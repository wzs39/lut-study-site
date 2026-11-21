(function (root, factory) {
  var api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.LUTSearch = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  function normalize(value) { return String(value || '').normalize('NFKC').toLowerCase().replace(/\s+/g, ' ').trim(); }
  function terms(query) { return Array.from(new Set(normalize(query).slice(0, 160).split(' ').filter(Boolean))).slice(0, 16); }
  function search(documents, query, filters) {
    var tokens = terms(query); filters = filters || {};
    if (!tokens.length) return [];
    return documents.reduce(function (results, doc) {
      if ((filters.course && doc.course !== filters.course) || (filters.kind && doc.kind !== filters.kind)) return results;
      var title = normalize(doc.title + ' ' + (doc.lectureTitle || ''));
      var metadata = normalize([doc.course, doc.courseTitle, doc.part].concat(doc.keywords || []).join(' '));
      var body = normalize(doc.text), all = title + ' ' + metadata + ' ' + body;
      if (tokens.every(function (word) { return all.includes(word); })) {
        var score = tokens.reduce(function (n, word) {
          return n + (title.includes(word) ? 12 : 0) + (metadata.includes(word) ? 4 : 0) + (body.includes(word) ? 2 : 0);
        }, 0);
        results.push({ doc: doc, score: score });
      }
      return results;
    }, []).sort(function (a, b) { return b.score - a.score || a.doc.id.localeCompare(b.doc.id); });
  }
  function snippet(text, query, length) {
    text = String(text || ''); length = Math.max(30, length || 160);
    var folded = text.toLowerCase(), offsets = terms(query).map(function (word) { return folded.indexOf(word); }).filter(function (i) { return i >= 0; });
    var start = offsets.length ? Math.max(0, Math.min.apply(null, offsets) - Math.floor(length / 3)) : 0;
    return (start ? '…' : '') + text.slice(start, start + length) + (start + length < text.length ? '…' : '');
  }
  function segments(text, query) {
    text = String(text || '');
    var words = terms(query).sort(function (a, b) { return b.length - a.length; });
    if (!words.length) return [{ text: text, match: false }];
    var pattern = new RegExp(words.map(function (s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }).join('|'), 'gi');
    var result = [], index = 0, match;
    while ((match = pattern.exec(text))) {
      if (match.index > index) result.push({ text: text.slice(index, match.index), match: false });
      result.push({ text: match[0], match: true }); index = pattern.lastIndex;
    }
    if (index < text.length) result.push({ text: text.slice(index), match: false });
    return result;
  }
  return { normalize: normalize, terms: terms, search: search, snippet: snippet, segments: segments };
});
