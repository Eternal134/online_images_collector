var downloader = function () {
    function e(e) {
        var t = e.bigUrl || e.originalUrl, n = "jpg", a = e.alt, i = t.lastIndexOf("/"), l = t.substr(i + 1, t.length);
        (i = l.lastIndexOf("?")) >= 0 && (l = l.substr(0, i)), (i = l.lastIndexOf(".")) >= 0 && (n = l.substr(i + 1, l.length), l = l.substr(0, i));
        l = l + "." + (n = ("jpeg" == e.ext ? "jpg" : e.ext) || n);
        "original" != r.filenameAltOrOriginal && e.group && (l = e.group + "-" + l), a && "alt" == r.filenameAltOrOriginal && (l = a + "." + n), l.lastIndexOf(".") < 0 && (l += ".jpg");
        var o = l;
        try {
            o = decodeURIComponent(l)
        } catch (e) {
        }
        var s = (o = (o = (o = o.replace(/^ +/, "")).replace(/ +$/, "")).replace(/ /g, "_yythkg_")).replace(/[/~|\\:*?"'<>=%$@#+;,!\^\s]/g, "_").replace(/\.+$/g, "").split(".");
        s[0] = utils.getSafeDir(s[0].substr(0, 100)), s = s.join("."), r.needRename && (s = utils.replaceVarible({
            text: r.renameRule || r.defaultConfig.renameRule,
            index: e.selected ? e.selectIndex : e.showIndex,
            ext: n,
            name: s,
            pageTitle: e.docTitle
        }));
        var u = s;
        return "FIXED" == r.dirType ? r.fixedDir && (u = utils.getSafeDir(r.fixedDir) + "/" + s) : e.docTitle && (u = utils.getSafeDir(e.docTitle) + "/" + s), u = u.replace(/_yythkg_/g, " ")
    }

    function t(t) {
        if (t) {
            var n = t.bigUrl, a = t.blobUrl, l = e(t), o = a || n;
            r.autoConvertWebp && t.jpgPngDataUrl && (o = t.jpgPngDataUrl), "VIDEO" == t.type && (o = t.originalUrl), chrome.downloads.download({
                url: o,
                filename: l,
                saveAs: !1,
                conflictAction: "uniquify"
            }, function (r) {
                if (r && (i[r] = t), !r && chrome.runtime.lastError && chrome.runtime.lastError.message.match("Invalid filename")) {
                    var a = t.ref;
                    a && (a = (a = a.replace(/.*?:\/\//, "")).replace(/\?.*/, "")), a.match("/$") || (a += "/");
                    var l = e({bigUrl: t.bigUrl, alt: t.showIndex + 1 + ""});
                    chrome.downloads.download({
                        url: n,
                        filename: a + l,
                        saveAs: !1,
                        conflictAction: "uniquify"
                    }, function (e) {
                        i[e] = t
                    })
                }
            })
        }
    }

    chrome.downloads.onChanged.addListener(function (e) {
        if (e.state && r.limitConcurrent && e.state.current.match("complete|interrupted")) {
            var o = i[e.id];
            if (o && (n(e.state.current, o), l < a.length)) {
                var s = a[l];
                "started" != downloader.status && "resumed" != downloader.status || (l++, t(s))
            }
        }
    });
    var r, n, a = [], i = [], l = 0;
    return {
        status: "not-inited", init: function (e, t) {
            r = e, n = t, l = 0
        }, download: function (e) {
            a = e, l = 0, a = e;
            for (var n = r.limitConcurrent || 10, i = 0; i < n && i < a.length; i++) l++, t(a[i]);
            this.status = "started"
        }, downloadSingle: function (e) {
            t(e)
        }, stop: function () {
            this.status = "stoped"
        }, pause: function () {
            this.status = "paused"
        }, resume: function () {
            this.status = "resumed";
            for (var e = 0; e < r.limitConcurrent && l < a.length; e++) t(a[l++])
        }
    }
}();