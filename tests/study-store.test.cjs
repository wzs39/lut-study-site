const test=require('node:test');const assert=require('node:assert/strict');
const Store=require('../assets/study-store.js');
function memory(initial={}){const values=new Map(Object.entries(initial));return {getItem:k=>values.get(k)||null,setItem:(k,v)=>values.set(k,String(v))};}
test('migrates legacy review checks without deleting the old store',()=>{
 const storage=memory({'lut-review-v1':JSON.stringify({'1-one':true})});
 const store=Store.create(storage,{ids:['1/one'],now:()=>1000});
 assert.equal(store.getLecture('1/one').status,'mastered');
 store.setLecture('1/one',{status:'review'});
 assert.equal(JSON.parse(storage.getItem('lut-review-v1'))['1-one'],false);
 assert.equal(Store.create(storage,{ids:['1/one']}).getLecture('1/one').status,'review');
});
test('persists learning state and subsection, clamps unsafe preferences',()=>{
 const storage=memory();const store=Store.create(storage,{now:()=>1000});
 store.setLecture('1/one',{status:'learning',anchor:'sec-detail',ratio:8,visited:true});
 const next=Store.create(storage);assert.equal(next.getLecture('1/one').anchor,'sec-detail');
 assert.equal(next.getLecture('1/one').ratio,1);assert.equal(next.read().lastLecture,'1/one');
 next.setPreferences({fontSize:999,lineHeight:2.1,focus:true,evil:'x'});
 assert.equal(next.read().preferences.fontSize,17);assert.equal(next.read().preferences.lineHeight,2.1);
 assert(!('evil' in next.read().preferences));
});
test('preserves in-memory state and reports failed storage writes',()=>{
 const store=Store.create({getItem:()=>{throw Error('denied');},setItem:()=>{throw Error('denied');}});
 const result=store.setLecture('1/one',{status:'learning'});
 assert.equal(result.persisted,false);assert.equal(store.getLecture('1/one').status,'learning');
});
test('question states, bookmarks, safe import and export round trip',()=>{
 const store=Store.create(memory(),{now:()=>1000});
 store.setPractice('1/one/practice-1',{status:'wrong',bookmarked:true,prompt:'<img onerror=alert(1)> question'});
 const target=Store.create(memory());target.importData(store.exportData());
 assert.equal(target.read().practice['1/one/practice-1'].status,'wrong');
 assert.throws(()=>target.importData('{"version":99}'));
 assert.equal(target.read().practice['1/one/practice-1'].bookmarked,true);
 assert.throws(()=>store.setLecture('../escape',{status:'mastered'}));
});
