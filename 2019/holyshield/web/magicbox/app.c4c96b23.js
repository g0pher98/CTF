(function(e) {
	function t(t) {
		for (var n, i, l = t[0], f = t[1], c = t[2], s = 0, p = []; s < l.length; s++)
			i = l[s],
				Object.prototype.hasOwnProperty.call(a, i) && a[i] && p.push(a[i][0]),
				a[i] = 0;
		for (n in f)
			Object.prototype.hasOwnProperty.call(f, n) && (e[n] = f[n]);
		u && u(t);
		while (p.length)
			p.shift()();
		return o.push.apply(o, c || []),
			r()
	}
	function r() {
		for (var e, t = 0; t < o.length; t++) {
			for (var r = o[t], n = !0, l = 1; l < r.length; l++) {
				var f = r[l];
				0 !== a[f] && (n = !1)
			}
			n && (o.splice(t--, 1),
				e = i(i.s = r[0]))
		}
		return e
	}
	var n = {}
		, a = {
			app: 0
		}
		, o = [];
	function i(t) {
		if (n[t])
			return n[t].exports;
		var r = n[t] = {
			i: t,
			l: !1,
			exports: {}
		};
		return e[t].call(r.exports, r, r.exports, i),
			r.l = !0,
			r.exports
	}
	i.m = e,
		i.c = n,
		i.d = function(e, t, r) {
			i.o(e, t) || Object.defineProperty(e, t, {
				enumerable: !0,
				get: r
			})
		}
		,
		i.r = function(e) {
			"undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
				value: "Module"
			}),
				Object.defineProperty(e, "__esModule", {
					value: !0
				})
		}
		,
		i.t = function(e, t) {
			if (1 & t && (e = i(e)),
				8 & t)
				return e;
			if (4 & t && "object" === typeof e && e && e.__esModule)
				return e;
			var r = Object.create(null);
			if (i.r(r),
				Object.defineProperty(r, "default", {
					enumerable: !0,
					value: e
				}),
				2 & t && "string" != typeof e)
				for (var n in e)
				i.d(r, n, function(t) {
					return e[t]
				}
					.bind(null, n));
			return r
		}
		,
		i.n = function(e) {
			var t = e && e.__esModule ? function() {
				return e["default"]
			}
				: function() {
					return e
				}
			;
			return i.d(t, "a", t),
				t
		}
		,
		i.o = function(e, t) {
			return Object.prototype.hasOwnProperty.call(e, t)
		}
		,
		i.p = "/";
	var l = window["webpackJsonp"] = window["webpackJsonp"] || []
		, f = l.push.bind(l);
	l.push = t,
		l = l.slice();
	for (var c = 0; c < l.length; c++)
		t(l[c]);
	var u = f;
	o.push([0, "chunk-vendors"]),
		r()
}
)({
	0: function(e, t, r) {
		e.exports = r("56d7")
	},
	"034f": function(e, t, r) {
		"use strict";
		var n = r("64a9")
			, a = r.n(n);
		a.a
	},
	"36e1": function(e, t, r) {
		"use strict";
		var n = r("6af5")
			, a = r.n(n);
		a.a
	},
	"56d7": function(e, t, r) {
		"use strict";
		r.r(t);
		r("cadf"),
			r("551c"),
			r("f751"),
			r("097d");
		var n, a = r("5ee5"), o = r.n(a), i = function() {
			var e = this
				, t = e.$createElement
				, r = e._self._c || t;
			return r("div", {
				staticClass: "bg",
				attrs: {
					id: "app"
				}
			}, [r("br"), r("br"), r("br"), r("br"), r("br"), r("br"), r("br"), r("br"), r("br"), r("b-card", [r("b-card-text", [e._v("\n    Hi! You entered Howl's Magic Castle ! "), r("br"), e._v("\n    Show your magical ability using by this Magic Box! "), r("br"), r("input", {
				directives: [{
					name: "model",
					rawName: "v-model",
					value: e.template,
					expression: "template"
				}],
				attrs: {
					type: "text"
				},
				domProps: {
					value: e.template
				},
				on: {
					input: function(t) {
						t.target.composing || (e.template = t.target.value)
					}
				}
			}), 1 == e.vv ? r("v-runtime-template", {
				attrs: {
					template: "<Mag1c>" + e.template + "</Mag1c>"
				}
			}) : e._e(), r("label", [e._v(e._s(e.flag))])], 1)], 1)], 1)
		}, l = [], f = r("dd1e"), c = function(e, t) {
			var r = t._c;
			return r("div", {
				attrs: {
					id: "wrapper"
				}
			}, [t._t("default")], 2)
		}, u = [], s = (r("36e1"),
			r("2877")), p = {}, d = Object(s["a"])(p, c, u, !0, null, "6c46ea3c", null), h = d.exports, v = {
				ENC: "enc",
				ENC1: "enc2",
				ENC2: "enc3"
			}, b = {
				components: {
					VRuntimeTemplate: f["a"],
					Mag1c: h
				},
				data: function() {
					return {
						template: "",
						vv: 0,
						flag: ""
					}
				},
				name: "app",
				methods: {
					_0xabracada: function(e) {
						for (var t = new Array, r = 0, n = e, a = parseInt(n[0].charCodeAt(0) - 55296), o = 0; o <= 2 * ("z".charCodeAt() - a - 36); o += 2,
							r++) {
							if (26 != n.length)
								return this.flag = "fail.. :(",
									void (n = "");
							if (a < 10)
								return this.flag = "fail.. :(",
									void (n = "");
							t[o] = String.fromCharCode(36 + a + r),
								t[o + 1] = String.fromCharCode(4 + a + r)
						}
						var i = "";
						o = 0;
						while (o < n.length && "" != n) {
							if (n[o] <= 97 || n[o] >= 122)
								return this.flag = "fail.. :(",
									void (n = "");
							var l;
							if (l = n[o + 1].charCodeAt(0) - 56320,
								l < 0 && (l = n[o].charCodeAt(0)),
								o += 2,
								l - 500 < 0 || l > 551) {
								while (l > 51) {
									if (l - 551 <= t.length) {
										l -= 552;
										break
									}
									l = parseInt(l / t.length)
								}
								i += t[l]
							} else
								i += t[l - 500]
						}
						"" != n && (this.flag = "flag: " + i)
					}
				},
				created: function() {
					var e = navigator.userAgent.toLowerCase();
					-1 != e.indexOf("edge") ? (this.vv = 0,
						window.location.href = "https://bit.ly/12A4LFM") : -1 != e.indexOf("fire") ? (this.vv = 0,
							window.location.href = "https://bit.ly/12A4LFM") : -1 != e.indexOf("chrome") && (this.vv = 1)
				}
			}, g = b, m = (r("034f"),
				Object(s["a"])(g, i, l, !1, null, null, null)), w = m.exports, y = r("2f62"), C = r("bd86"), x = (n = {},
					Object(C["a"])(n, v.ENC, (function(e, t) {
						for (var r = ["charCodeAt", "fail.. :(", "length"], n = function(e, t) {
							e -= 0;
							var n = r[e];
							return n
						}, a = new Array, o = 0, i = t["command"], l = parseInt(i[0][n("0x0")](0) - 55296), f = 0; f <= 2 * ("z"[n("0x0")]() - l - 36); f += 2,
							o++) {
							if (26 != i["length"]) {
								alert("fail.. we need 26 length!!:("),
									i = "";
								break
							}
							if (l < 10) {
								alert(n("0x1")),
									i = "";
								break
							}
							a[f] = String["fromCharCode"](36 + l + o),
								a[f + 1] = String["fromCharCode"](4 + l + o)
						}
						var c = "";
						f = 0;
						while (f < i["length"] && "" != i) {
							if (i[f] <= 97 || i[f] >= 122) {
								alert("fail.. :( it's not printable!! 97 ~ 122"),
									i = "";
								break
							}
							var u;
							if (u = i[f + 1]["charCodeAt"](0) - 56320,
								u < 0 && (u = i[f][n("0x0")](0)),
								f += 2,
								u - 500 < 0 || u > 551) {
								while (u > 51) {
									if (u - 551 <= a["length"]) {
										u -= 552;
										break
									}
									u = parseInt(u / a[n("0x2")])
								}
								c += a[u]
							} else
								c += a[u - 500]
						}
						"" != i && alert("correct flag : " + c)
					}
					)),
					Object(C["a"])(n, v.ENC1, (function(e) {
						return "hi"
					}
					)),
					n);
		o.a.use(y["a"]);
		var O = new y["a"].Store({
			actions: x
		})
			, _ = O
			, j = r("5f5b");
		r("f9e3"),
			r("2dd8");
		o.a.use(j["a"]),
			o.a.config.productionTip = !1,
			new o.a({
				store: _,
				render: function(e) {
					return e(w)
				}
			}).$mount("#app")
	},
	"64a9": function(e, t, r) {},
	"6af5": function(e, t, r) {}
});

