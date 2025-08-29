<!DOCTYPE html>
<!-- saved from url=(0014)about:internet -->
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta http-equiv="X-UA-TextLayoutMetrics" content="gdi" />
<link rel="stylesheet" href="style.css" type="text/css"/>
<script type="text/javascript" src="chart.js"></script>
<script type="text/javascript">
//DATA
var data = [
		{name : 'Folder Sizes',value : 1,color:'#a47d7c',tp:'Folder sizes'}
];
//DATAEND

function RefreshChart()
{
	if (!Array.isArray(data) || !data.length) {	
		document.getElementById('canvasDiv').style.display = 'none';		
		return;
	}
	else
		document.getElementById('canvasDiv').style.display = 'block';		
	chart.load(data);
	chart.resize(window.innerWidth,window.innerHeight);
}	

function resizeChart() {
	chart.resize(window.innerWidth,window.innerHeight);
};

if (window.addEventListener)
	window.addEventListener('resize', resizeChart);
	
$(function(){
	var w = window.innerWidth;
	var h = window.innerHeight
	
	chart = new iChart.Pie2D({
		id:'mindgems_chart',
		render : 'canvasDiv',
		data: data,
		sub_option : {
			label : {
				background_color:null,
				sign:'square',
				sign_size:12,
				border:{
					enable:false
				},
				font: ' Tahoma',
				fontsize:12,
				fontweight : 'normal',
				color : '#000',
				color_factor : 0.001,
				text_with_sign_color : false,
				shadow : true,
				shadow_blur : 5,
				shadow_color : '#000000'
			},
			listeners:{
				click:function(s,e,m){
					if (s.get('name') == 'Others') return;
					external.ChartClicked(s.get('id'));
				},
				mouseout:function(s,e){
					chart.rebound(s.get('id'));
				}
			}			
		},
		tip:{					
			style:'textAlign:left;padding:4px;cursor:pointer;backgroundColor:rgba(239,239,239,.85);color:black;font:14px Tahoma;',
			enable:true,
			showType:'fixed',	
				listeners:{
					parseText:function(tip,name,value,text,i){
						if (typeof data === 'undefined' || data === null || (!Array.isArray(data)) || (!data.length)) {
							return '';
						};
						return data[i]['tp'];
					}
				}
		},
		color_factor:0.1,
		animation : true,
		animation_duration:300,
		shadow : true,
		shadow_blur : 3,
		shadow_color : '#000000',
		shadow_offsetx : 0,
		shadow_offsety : 0,
		background_color:'#F3F2F3',
		gradient:true,
		color_factor:0.2,
		gradient_mode:'LinearGradientDownUp',
		offset_angle:0,
		mutex : false,
		showpercent:true,
		decimalsnum:2,
		width: w,
		height: h,
		radius:'100%',
		bound_event:'mouseover',
	});
	chart.draw();
});
</script>

</head>
<body style="margin:0px; padding:0px;">
		<div id='canvasDiv'></div>
<!--[if lt IE 9 ]>
<p>Charts require Internet Explorer 9 or newer to be installed on the system. Upgrade Internet Explorer and restart the application to enable them.</p>
<![endif]-->
</body>
</html>

