var svg, po, map;
var radius = 10, tips = {}, xfocus = {};

function load(e) {
	for ( var i = 0; i < e.features.length; i++) {
		var f = e.features[i];
		f.element.id = "c" + f.data.id;
		f.element.setAttribute("r", radius);
		f.element.addEventListener("mouseover", toggle(f.data, f.element),
				false);
		f.element
				.addEventListener("mouseout", toggle(f.data, f.element), false);
		f.element.addEventListener("mousedown", fnfocus(f.data, f), false);
	}
}
function openIncidentPanel(id) {
	$('#connectivity').removeClass('closed').addClass('open');
	$('#panel_connectivity').show();
	$('#' + id).removeClass('closed').addClass('open');
	$('#panel_' + id).show();
}
function fnfocus(d, f) {
	var fn = xfocus[d.id];
	if (!fn) {
		fn = {
			id : d.id,
			feature : f,
			highligh : function(e) {
				fn.feature.element.setAttribute("r", radius * 2);
				openIncidentPanel(fn.id);
				$.scrollTo('#'+fn.id);
			}
		}
	}
	return fn.highligh;
}

function show(e) {
	for ( var i = 0; i < e.features.length; i++) {
		var f = e.features[i], tip = tips[f.data.id];
		tip.feature = f.data;
		tip.location = {
			lat : f.data.geometry.coordinates[1],
			lon : f.data.geometry.coordinates[0]
		};
		update(tip);
	}
}

function move() {
	for ( var id in tips) {
		update(tips[id]);
	}
}

function cancel(e) {
	e.stopPropagation();
	e.preventDefault();
}
function update(tip) {
	if (!tip.visible)
		return; // ignore
	var p = map.locationPoint(tip.location);
	var o = $('#map').offset();
	tip.anchor.style.left = o.left + p.x - radius + "px";
	tip.anchor.style.top = o.top + p.y - radius + "px";
	$(tip.anchor).tipsy("show");
}

function toggle(f) {
	var tip = tips[f.id];
	if (!tip) {
		tip = tips[f.id] = {
			id : f.id,
			anchor : document.body.appendChild(document.createElement("a")),
			visible : false,
			toggle : function(e) {
				tip.visible = !tip.visible;
				update(tip);
				$(tip.anchor).tipsy(tip.visible ? "show" : "hide");
				cancel(e);
				$('#c' + tip.id).attr("r", tip.visible ? 2 * radius : radius);
				if (tip.visible) {
					$('#l' + tip.id).addClass('highlighted');
				} else {
					$('#l' + tip.id).removeClass('highlighted');
				}
				// TODO: jQuery animation doesn't work. Use D3 instead.
				// $('#c'+tip.id).animate({"r":tip.visible?2*radius:radius+"px"},1000);
			}
		};
		tip.anchor.id = '_' + f.id;
		tip.anchor.style.position = "absolute";
		tip.anchor.style.visibility = "hidden";
		tip.anchor.style.width = radius * 2 + "px";
		tip.anchor.style.height = radius * 2 + "px";
		$(tip.anchor).tipsy({
			html : true,
			fallback : f.properties.html,
			gravity : $.fn.tipsy.autoNS,
			trigger : "manual"
		});
	}
	return tip.toggle;
}

function setupMap(args) {
	var feat = args.features;
	po = org.polymaps;
	svg = po.svg("svg");
	svg.setAttribute('width', '100%');
	svg.setAttribute('height', '100%');
	map = po.map()
			.container(document.getElementById("map").appendChild(svg))
			.zoomRange([ 1, 16 ])
			.add(po.drag());

	map.add(po.image().url(
			po.url(
					"http://{S}tile.cloudmade.com" + "/" + args.api_key
							+ "/48233/256/{Z}/{X}/{Y}.png").hosts(
					[ "a.", "b.", "c.", "" ])));
	map.add(po.geoJson().on("load", load).on("show", show).features(feat).clip(
			false).scale('fixed'));

	map.extent(args.extent).zoomBy(-1);

	$('a.panel').mouseenter(function() {
		var panel = $(this);
		var id = panel.attr('id');
		$('#c' + id).attr("r", 2 * radius);
	});
	$('a.panel').mouseleave(function() {
		var panel = $(this);
		var id = panel.attr('id');
		$('#c' + id).attr("r", radius);
	});
	return map;
}