(function (root, factory) {
  var api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.LUTStudyStore = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  var KEY = 'lut-learning-v1', LEGACY = 'lut-review-v1';
  var STATUSES = ['new', 'learning', 'review', 'mastered'];
  var PRACTICE = ['todo', 'done', 'wrong', 'retry'];
  var ID = /^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$/;
  var QUESTION = /^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+\/practice-[1-9]\d*$/;
  function object(value) { return value && typeof value === 'object' && !Array.isArray(value); }
  function text(value, max) { return typeof value === 'string' ? value.slice(0, max) : ''; }
  function time(value) { return Number.isFinite(value) ? Math.max(0, Math.min(4102444800000, value)) : 0; }
  function defaults() { return { schema:'lut-learning', version:1, lectures:{}, practice:{}, preferences:{fontSize:17,lineHeight:1.85,focus:false}, lastLecture:'' }; }
  function lecture(value) {
    value = object(value) ? value : {};
    return {status:STATUSES.includes(value.status) ? value.status : 'new',
      anchor:/^[A-Za-z0-9_-]{1,160}$/.test(value.anchor || '') ? value.anchor : '',
      ratio:Number.isFinite(value.ratio) ? Math.max(0, Math.min(1, value.ratio)) : 0,
      revision:/^[a-f0-9]{12}$/.test(value.revision || '') ? value.revision : '',
      updatedAt:time(value.updatedAt), visitedAt:time(value.visitedAt)};
  }
  function preferences(value) {
    value = object(value) ? value : {};
    return {fontSize:[17,19,22].includes(value.fontSize) ? value.fontSize : 17,
      lineHeight:[1.65,1.85,2.1].includes(value.lineHeight) ? value.lineHeight : 1.85, focus:value.focus === true};
  }
  function clean(value) {
    var result = defaults();
    if (!object(value) || value.version !== 1) return result;
    Object.keys(object(value.lectures) ? value.lectures : {}).forEach(function (id) {
      if (ID.test(id)) result.lectures[id] = lecture(value.lectures[id]);
    });
    Object.keys(object(value.practice) ? value.practice : {}).forEach(function (id) {
      var row = value.practice[id];
      if (!QUESTION.test(id) || !object(row)) return;
      result.practice[id] = {status:PRACTICE.includes(row.status) ? row.status : 'todo', bookmarked:row.bookmarked === true,
        prompt:text(row.prompt,1200), updatedAt:time(row.updatedAt)};
    });
    result.preferences = preferences(value.preferences);
    result.lastLecture = ID.test(value.lastLecture || '') ? value.lastLecture : '';
    return result;
  }
  function create(storage, options) {
    options = options || {};
    var clock = options.now || Date.now, memory = defaults(), dirty = false;
    function read() {
      var state = memory;
      if (!dirty) {
        try { state = clean(JSON.parse(storage.getItem(KEY) || 'null')); } catch (_) { state = clean(memory); }
        try {
          var old = JSON.parse(storage.getItem(LEGACY) || '{}');
          (options.ids || []).forEach(function (id) {
            if (ID.test(id) && !state.lectures[id] && old[id.replace('/', '-')] === true) state.lectures[id] = lecture({status:'mastered'});
          });
        } catch (_) { /* Corrupt legacy data must not prevent reading current progress. */ }
      }
      memory = clean(state); return clean(memory);
    }
    function save(state, legacyId) {
      memory = clean(state);
      try {
        storage.setItem(KEY, JSON.stringify(memory));
        if (legacyId) {
          var old;
          try { old = JSON.parse(storage.getItem(LEGACY) || '{}'); } catch (_) { old = {}; }
          if (!object(old)) old = {};
          (Array.isArray(legacyId) ? legacyId : [legacyId]).forEach(function(id){old[id.replace('/', '-')] = memory.lectures[id].status === 'mastered';});
          storage.setItem(LEGACY, JSON.stringify(old));
        }
        dirty = false; return {state:clean(memory), persisted:true};
      } catch (_) { dirty = true; return {state:clean(memory), persisted:false}; }
    }
    function setLecture(id, patch) {
      if (!ID.test(id)) throw new Error('讲义标识无效');
      var state = read(), current = state.lectures[id] || lecture({});
      patch = patch || {};
      state.lectures[id] = lecture(Object.assign({}, current, patch, {updatedAt:clock()}));
      if (patch.visited) { state.lastLecture = id; state.lectures[id].visitedAt = clock(); }
      return save(state, Object.hasOwn(patch, 'status') ? id : null);
    }
    function setPractice(id, patch) {
      if (!QUESTION.test(id)) throw new Error('练习标识无效');
      var state = read();
      state.practice[id] = Object.assign({status:'todo',bookmarked:false,prompt:''}, state.practice[id] || {}, patch || {}, {updatedAt:clock()});
      return save(state);
    }
    function setPreferences(patch) {
      var state = read(); state.preferences = preferences(Object.assign({},state.preferences,patch)); return save(state);
    }
    function importData(serialized) {
      if (typeof serialized !== 'string' || serialized.length > 2000000) throw new Error('备份文件过大或格式无效');
      var incoming = JSON.parse(serialized);
      if (!object(incoming) || incoming.schema !== 'lut-learning' || incoming.version !== 1 || !object(incoming.lectures) || !object(incoming.practice)) throw new Error('请选择本站导出的学习记录备份');
      Object.entries(incoming.lectures).forEach(function (entry) {
        if (!ID.test(entry[0]) || !object(entry[1]) || !STATUSES.includes(entry[1].status)) throw new Error('备份含无效讲义记录');
      });
      Object.entries(incoming.practice).forEach(function (entry) {
        if (!QUESTION.test(entry[0]) || !object(entry[1]) || !PRACTICE.includes(entry[1].status)) throw new Error('备份含无效练习记录');
      });
      var state = read(), next = clean(incoming);
      ['lectures','practice'].forEach(function (key) {
        Object.keys(next[key]).forEach(function (id) {
          if (!state[key][id] || next[key][id].updatedAt >= state[key][id].updatedAt) state[key][id] = next[key][id];
        });
      });
      state.preferences = next.preferences;
      if (next.lastLecture) state.lastLecture = next.lastLecture;
      return save(state,Object.keys(state.lectures));
    }
    return {read:read,getLecture:function(id){return read().lectures[id] || lecture({});},
      setLecture:setLecture,setPractice:setPractice,setPreferences:setPreferences,
      exportData:function(){return JSON.stringify(read(),null,2);},importData:importData};
  }
  return {create:create,statuses:STATUSES,practiceStatuses:PRACTICE,key:KEY,legacyKey:LEGACY};
});
