const test = require('node:test');
const assert = require('node:assert/strict');
const Search = require('../assets/search-core.js');
const docs = [
  {id:'a',course:'1',kind:'detail',title:'变量',lectureTitle:'第一讲',keywords:['type'],text:'正文中特有的浮点误差 hidden phrase'},
  {id:'b',course:'2',kind:'practice',title:'矩阵练习',lectureTitle:'第二讲',keywords:[],text:'matrix inverse hidden phrase'},
];
test('searches body with AND tokens, case folding and course/section filters', () => {
  assert.equal(Search.search(docs,'HIDDEN phrase').length,2);
  assert.equal(Search.search(docs,'正文中特有')[0].doc.id,'a');
  assert.equal(Search.search(docs,'hidden',{course:'2'})[0].doc.id,'b');
  assert.equal(Search.search(docs,'hidden',{kind:'practice'})[0].doc.id,'b');
  assert.equal(Search.search(docs,'hidden missing').length,0);
  assert.equal(Search.search(docs,'').length,0);
});
test('prefers title matches and returns bounded snippets', () => {
  assert.equal(Search.search(docs,'矩阵')[0].doc.id,'b');
  const snippet=Search.snippet('x'.repeat(300)+'needle'+'z'.repeat(300),'needle',100);
  assert(snippet.includes('needle'));assert(snippet.length<=104);
});
test('highlight segments remain text, including markup-like input', () => {
  const text='<img src=x onerror=alert(1)> hidden';
  const parts=Search.segments(text,'<img');
  assert.equal(parts.map(x=>x.text).join(''),text);
  assert(parts.some(x=>x.match));
  assert(parts.every(x=>typeof x.text==='string'));
});
