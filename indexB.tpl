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

$(function() {
	var w = window.innerWidth;
	var h = window.innerHeight

	chart = new iChart.Column3D({
			id: 'mindgems_chart',
			render : 'canvasDiv',
			data: data,
			width : w,
			height : h,
			padding: 0,
			animation : true,
			animation_duration:100,
			shadow: true,
			shadow_blur : 10,
			shadow_offsetx : 2,
			shadow_offsety : 1,			
			background_color:'#f8f8f8',
			xAngle:70,
			yAngle:15,
			column_width:80,
			sub_option:{
				label : {
				padding:'10 -40',
				border:{
					enable:false
				},
				font: ' Tahoma',
				fontsize:12,
				fontweight : 'normal',
				color : '#000',
				color_factor : 0.001,
				text_with_sign_color : true,
				shadow : true,
				shadow_blur : 3,
				shadow_color : '#FFFFFF',
				},
				listeners:{
					parseText:function(r,t){
						return t+'%';
					},
					click:function(s,e,m){
						if (s.get('name') == 'Others') return;
						external.ChartClicked(s.get('id'));
					}					
				}
			},
			coordinate:{
				background_color : '#F0F0FF',
				color_factor: 0.07,			
				grid_color : '#B0B0B0',
				left_board:false,
				width:'95%',
				offsetx: -10,
				scale:[{
					 label:{color:'#202020',font:'Tahoma',fontsize:10},
					 position:'left',
					 start_scale:0,
					 end_scale:100,
					 scale_space:10,
					 listeners:{
							parseText:function(t,x,y){
								return {text:t}
							}
						}
				}],
			},
			label : {
				font : 'Tahoma',
				fontsize:12,
				fontweight:'normal',
				textAlign:'right',
				textBaseline:'middle',
				rotate:350,
				color : '#000000',
				offsetx : 30,
				shadow : true,
				shadow_blur : 3,
				shadow_color : '#FFFFFF',
			},
			tip:{
				enable:true,
				move_duration : 100,
				style:'textAlign:left;padding:4px;cursor:pointer;backgroundColor:rgba(239,239,239,.85);color:black;font:14px Tahoma;',
				listeners:{
					parseText:function(tip,name,value,text,i){
						if (typeof data === 'undefined' || data === null || (!Array.isArray(data)) || (!data.length)) {
							return '';
						};
						return data[i]['tp'];
					}
				}
			},
		});
	chart.draw();
});
</script>
</head>
<body style="margin:0px; padding:0px; ">
		<div id='canvasDiv'></div>
<!--[if lt IE 9 ]>
<p>Charts require Internet Explorer 9 or newer to be installed on the system. Upgrade Internet Explorer and restart the application to enable them.</p>
<![endif]-->
</body>
</html>
