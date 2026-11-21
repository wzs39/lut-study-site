const test=require('node:test'),assert=require('node:assert/strict');
const config=require('../assets/sharing-config.js');
test('accepts public project configuration and rejects secret keys and URL credentials',()=>{
  assert.equal(config.validate({supabaseUrl:'https://example.supabase.co/',supabaseAnonKey:'sb_publishable_test'}).supabaseUrl,'https://example.supabase.co');
  for(const key of ['sb_secret_test','not-a-key'])assert.throws(()=>config.validate({supabaseUrl:'https://example.supabase.co',supabaseAnonKey:key}));
  for(const url of ['javascript:alert(1)','http://example.org','https://user:pass@example.org','https://example.org/path'])assert.throws(()=>config.validate({supabaseUrl:url,supabaseAnonKey:'sb_publishable_test'}));
  const token='x.'+Buffer.from(JSON.stringify({role:'service_role'})).toString('base64url')+'.x';
  assert.throws(()=>config.validate({supabaseUrl:'https://example.supabase.co',supabaseAnonKey:token}));
});
test('publishable keys use apikey only while legacy anon JWT keeps Bearer compatibility',()=>{
  assert.deepEqual(config.headers('sb_publishable_test'),{apikey:'sb_publishable_test'});
  assert.deepEqual(config.headers('a.b.c',{'Content-Type':'application/json'}),{apikey:'a.b.c',Authorization:'Bearer a.b.c','Content-Type':'application/json'});
});
