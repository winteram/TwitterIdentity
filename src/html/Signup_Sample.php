2 requests  ❘  38.57KB transferred  ❘  369ms (onload: 373ms, DOMContentLoaded: 383ms)
signupforexp.php
/expersub
53ms0
showdaily.php
/expersub
193ms176ms

HeadersPreviewResponseCookiesTiming
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
  "http://www.w3.org/TR/html4/strict.dtd">
<html lang="en">
<head>
  <title>Psychological and Brain Sciences Experiment Administration</title>

<!-- styles suitable for any browser, any media -->
<style type="text/css" title="Site default">
body {
  background-color: #fff5e1;
  color: #000;
  font-size:85%;
}
</style>

<!-- hide these rules from legacy browsers and mobile devices -->
<style type="text/css" title="Site default" media="all">
@media screen, projection {
/* exploit a parsing bug so @media rules are visible to MacIE5 */
.BeNiceToMacIE5 {
  font-family: "\"}\"";
  font-family: inherit;
}
body {
  background-color: #fffaf0;
  color: #000;
}
.wrapper {
  margin: 1% 3%;
  padding: 0;
  border: thin solid #7d5500;
}

.colorbutton
{
	background-color: #ccffff;
	border:.1em outset;
}
h1 {
  background-color: #fcead7;    /* different color than content */
  color: #7d5500;
  margin: 0;
  padding: .2em 2%;
}
h1.header {
  background-color: #ccffff;    /* different color than content */
  color: #7d5500;
  margin: 0;
  padding: .2em 2%;
}
h3 {
  background-color: #fcead7;    /* different color than content */
  color: #7d5500;
  margin: 0;
  padding: .2em 2%;
}
h2 {
  margin: .2em 0;
}
.main {
  clear: both;
  width: 100%;
  margin: 0;
  padding: 0;
  border-top: thin solid #7d5500;
  border-bottom: thin solid #7d5500;
  color: #000;
}
.content {
  width: 80%;
  float: right;
  margin: 0;
  padding: 1% 2%;
}
.sidebar {
  margin-right: 85%;
  padding: 1%;
  font-size: 90%;
  border-right:2px dotted;
}
.clear {
  clear: both;
  height: 1px;
  overflow: hidden;   /* prevent IE expanding the container */
  margin: 0;          /* keep flush with surrounding blocks */
}
.footer {
  background-color: #ccffff;  /* same bg color as h1 */
  color: #7d5500;
  margin: 0;          /* flush with .main */
  padding: 1% 2%;
  font-size:12px;
  text-align:center;
}
.nav {
  border-top: thin solid #7d5500;
  font-size: 90%;
}
.nav ul {
  margin: .3em;
  padding: 0;
}
.nav li {
  list-style: none;
/*  display: inline; */
  float: left;
  padding: .5em 1em;
}
} /* end media rules */
</style>
<!-- protect other browsers from IE6's quirks -->
<!--[if IE 6]><style type="text/css" title="Site default">
h1, .sidebar {position:relative}</style><![endif]-->

</head>


<style type="text/css">

.ds_box {
	background-color: #FFF;
	border: 1px solid #000;
	position: absolute;
	z-index: 32767;
}

.ds_tbl {
	background-color: #FFF;
}

.ds_head {
	background-color: #333;
	color: #FFF;
	font-family: Arial, Helvetica, sans-serif;
	font-size: 13px;
	font-weight: bold;
	text-align: center;
	letter-spacing: 2px;
}

.ds_subhead {
	background-color: #CCC;
	color: #000;
	font-size: 12px;
	font-weight: bold;
	text-align: center;
	font-family: Arial, Helvetica, sans-serif;
	width: 32px;
}

.ds_cell {
	background-color: #EEE;
	color: #000;
	font-size: 13px;
	text-align: center;
	font-family: Arial, Helvetica, sans-serif;
	padding: 5px;
	cursor: pointer;
}

.ds_cell:hover {
	background-color: #F3F3F3;
} /* This hover code won't work for IE */

</style>
</head>
<body>

<table class="ds_box" cellpadding="0" cellspacing="0" id="ds_conclass" style="display: none;">
<tr><td id="ds_calclass">
</td></tr>
</table>

<script type="text/javascript">
// <!-- <![CDATA[

// Project: Dynamic Date Selector (DtTvB) - 2006-03-16
// Script featured on JavaScript Kit- http://www.javascriptkit.com
// Code begin...
// Set the initial date.
var ds_i_date = new Date();
ds_c_month = ds_i_date.getMonth() + 1;
ds_c_year = ds_i_date.getFullYear();

// Get Element By Id
function ds_getel(id) {
	return document.getElementById(id);
}

// Get the left and the top of the element.
function ds_getleft(el) {
	var tmp = el.offsetLeft;
	el = el.offsetParent
	while(el) {
		tmp += el.offsetLeft;
		el = el.offsetParent;
	}
	return tmp;
}
function ds_gettop(el) {
	var tmp = el.offsetTop;
	el = el.offsetParent
	while(el) {
		tmp += el.offsetTop;
		el = el.offsetParent;
	}
	return tmp;
}

// Output Element
var ds_oe = ds_getel('ds_calclass');
// Container
var ds_ce = ds_getel('ds_conclass');

// Output Buffering
var ds_ob = ''; 
function ds_ob_clean() {
	ds_ob = '';
}
function ds_ob_flush() {
	ds_oe.innerHTML = ds_ob;
	ds_ob_clean();
}
function ds_echo(t) {
	ds_ob += t;
}

var ds_element; // Text Element...

var ds_monthnames = [
'January', 'February', 'March', 'April', 'May', 'June',
'July', 'August', 'September', 'October', 'November', 'December'
]; // You can translate it for your language.

var ds_daynames = [
'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'
]; // You can translate it for your language.

// Calendar template
function ds_template_main_above(t) {
	return '<table cellpadding="3" cellspacing="1" class="ds_tbl">'
	     + '<tr>'
		 + '<td class="ds_head" style="cursor: pointer" onclick="ds_py();">&lt;&lt;</td>'
		 + '<td class="ds_head" style="cursor: pointer" onclick="ds_pm();">&lt;</td>'
		 + '<td class="ds_head" style="cursor: pointer" onclick="ds_hi();" colspan="3">[Close]</td>'
		 + '<td class="ds_head" style="cursor: pointer" onclick="ds_nm();">&gt;</td>'
		 + '<td class="ds_head" style="cursor: pointer" onclick="ds_ny();">&gt;&gt;</td>'
		 + '</tr>'
	     + '<tr>'
		 + '<td colspan="7" class="ds_head">' + t + '</td>'
		 + '</tr>'
		 + '<tr>';
}

function ds_template_day_row(t) {
	return '<td class="ds_subhead">' + t + '</td>';
	// Define width in CSS, XHTML 1.0 Strict doesn't have width property for it.
}

function ds_template_new_week() {
	return '</tr><tr>';
}

function ds_template_blank_cell(colspan) {
	return '<td colspan="' + colspan + '"></td>'
}

function ds_template_day(d, m, y) {
	return '<td class="ds_cell" onclick="ds_onclick(' + d + ',' + m + ',' + y + ')">' + d + '</td>';
	// Define width the day row.
}

function ds_template_main_below() {
	return '</tr>'
	     + '</table>';
}

// This one draws calendar...
function ds_draw_calendar(m, y) {
	// First clean the output buffer.
	ds_ob_clean();
	// Here we go, do the header
	ds_echo (ds_template_main_above(ds_monthnames[m - 1] + ' ' + y));
	for (i = 0; i < 7; i ++) {
		ds_echo (ds_template_day_row(ds_daynames[i]));
	}
	// Make a date object.
	var ds_dc_date = new Date();
	ds_dc_date.setDate(1);
	ds_dc_date.setMonth(m - 1);
	ds_dc_date.setFullYear(y);
	if (m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12) {
		days = 31;
	} else if (m == 4 || m == 6 || m == 9 || m == 11) {
		days = 30;
	} else {
		days = (y % 4 == 0) ? 29 : 28;
	}
	var first_day = ds_dc_date.getDay();
	var first_loop = 1;
	// Start the first week
	ds_echo (ds_template_new_week());
	// If sunday is not the first day of the month, make a blank cell...
	if (first_day != 0) {
		ds_echo (ds_template_blank_cell(first_day));
	}
	var j = first_day;
	for (i = 0; i < days; i ++) {
		// Today is sunday, make a new week.
		// If this sunday is the first day of the month,
		// we've made a new row for you already.
		if (j == 0 && !first_loop) {
			// New week!!
			ds_echo (ds_template_new_week());
		}
		// Make a row of that day!
		ds_echo (ds_template_day(i + 1, m, y));
		// This is not first loop anymore...
		first_loop = 0;
		// What is the next day?
		j ++;
		j %= 7;
	}
	// Do the footer
	ds_echo (ds_template_main_below());
	// And let's display..
	ds_ob_flush();
	// Scroll it into view.
	ds_ce.scrollIntoView();
}

// A function to show the calendar.
// When user click on the date, it will set the content of t.
function ds_sh(t) {
	// Set the element to set...
	ds_element = t;
	// Make a new date, and set the current month and year.
	var ds_sh_date = new Date();
	ds_c_month = ds_sh_date.getMonth() + 1;
	ds_c_year = ds_sh_date.getFullYear();
	// Draw the calendar
	ds_draw_calendar(ds_c_month, ds_c_year);
	// To change the position properly, we must show it first.
	ds_ce.style.display = '';
	// Move the calendar container!
	the_left = ds_getleft(t);
	the_top = ds_gettop(t) + t.offsetHeight;
	ds_ce.style.left = the_left + 'px';
	ds_ce.style.top = the_top + 'px';
	// Scroll it into view.
	ds_ce.scrollIntoView();
}

// Hide the calendar.
function ds_hi() {
	ds_ce.style.display = 'none';
}

// Moves to the next month...
function ds_nm() {
	// Increase the current month.
	ds_c_month ++;
	// We have passed December, let's go to the next year.
	// Increase the current year, and set the current month to January.
	if (ds_c_month > 12) {
		ds_c_month = 1; 
		ds_c_year++;
	}
	// Redraw the calendar.
	ds_draw_calendar(ds_c_month, ds_c_year);
}

// Moves to the previous month...
function ds_pm() {
	ds_c_month = ds_c_month - 1; // Can't use dash-dash here, it will make the page invalid.
	// We have passed January, let's go back to the previous year.
	// Decrease the current year, and set the current month to December.
	if (ds_c_month < 1) {
		ds_c_month = 12; 
		ds_c_year = ds_c_year - 1; // Can't use dash-dash here, it will make the page invalid.
	}
	// Redraw the calendar.
	ds_draw_calendar(ds_c_month, ds_c_year);
}

// Moves to the next year...
function ds_ny() {
	// Increase the current year.
	ds_c_year++;
	// Redraw the calendar.
	ds_draw_calendar(ds_c_month, ds_c_year);
}

// Moves to the previous year...
function ds_py() {
	// Decrease the current year.
	ds_c_year = ds_c_year - 1; // Can't use dash-dash here, it will make the page invalid.
	// Redraw the calendar.
	ds_draw_calendar(ds_c_month, ds_c_year);
}

// Format the date to output.
function ds_format_date(d, m, y) {
	// 2 digits month.
	m2 = '00' + m;
	m2 = m2.substr(m2.length - 2);
	// 2 digits day.
	d2 = '00' + d;
	d2 = d2.substr(d2.length - 2);
	// YYYY-MM-DD
	return y + '-' + m2 + '-' + d2;
}

// When the user clicks the day.
function ds_onclick(d, m, y) {
	// Hide the calendar.
	ds_hi();
	ds_element.value = ds_format_date(d, m, y);
	location.href="showdaily.php?dt="+ds_format_date(d, m, y);
}

// And here is the end.

// ]]> -->
</script>
<body>

<div class="wrapper">
<h1 class="header">Psychological and Brain Sciences Participation Management</h1>


<div class="main">

<div class="content"><!-- start content -->

<span style='font-size:20px;font-weight:bold'>Experiments Listed for <input onclick='ds_sh(this);' name='date' readonly='readonly' style='cursor: text' value='2012-09-13'></span><span style='color:red'><-- click to select a new date</span><table border=0 cellspacing=5 cellpadding=5><tr><td valign=top></td><td valign=top><table border=0 cellspacing=5 cellpadding=5><tr><td><b>Time</b></td><td><b>Name</b></td><td><b>Credit</b></td><td><b>Description</b></td><td><b>Eligibility</b></td><td><b>Seats Available</b></td></tr><tr style='background-color:#fcead7'><td><b>9:00 am</b></td><td><a href='listsession.php?sd=2012-09-13&st=09:00:00'><span 	style='font-size:12px'>prediction</span></a></td><td>1</td><td><span 	style='font-size:12px'>You will complete several personality surveys on a desktop computer and complete a short exercise in which you edit a paragraph in microsoft word.  The study should take about 30 minutes.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>1</td><tr style='background-color:#ffffff'><td><b>9:15 am</b></td><td><a href='listsession.php?sd=2012-09-13&st=09:15:00'><span 	style='font-size:12px'>prediction</span></a></td><td>1</td><td><span 	style='font-size:12px'>You will complete several personality surveys on a desktop computer and complete a short exercise in which you edit a paragraph in microsoft word.  The study should take about 30 minutes.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>7</td><tr style='background-color:#fcead7'><td><b>9:30 am</b></td><td><a href='listsession.php?sd=2012-09-13&st=09:30:00'><span 	style='font-size:12px'>Categorizing Alien Cells</span></a></td><td>1</td><td><span 	style='font-size:12px'>You will see alien cells and will be asked to categorize them into different species as accurately as possible, with feedback from the computer.  The experiment explores how people perceive and learn new concepts. </span></td><td><span 	style='font-size:12px'><br/></span></td><td>5</td><tr style='background-color:#ffffff'><td></td><td><a href='listsession.php?sd=2012-09-13&st=09:30:00'><span style='font-size:12px'>prediction</span></a></td><td>1</td><td><span style='font-size:12px'>You will complete several personality surveys on a desktop computer and complete a short exercise in which you edit a paragraph in microsoft word.  The study should take about 30 minutes.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>6</td></td><tr style='background-color:#fcead7'><td><b>9:45 am</b></td><td><a href='listsession.php?sd=2012-09-13&st=09:45:00'><span 	style='font-size:12px'>prediction</span></a></td><td>1</td><td><span 	style='font-size:12px'>You will complete several personality surveys on a desktop computer and complete a short exercise in which you edit a paragraph in microsoft word.  The study should take about 30 minutes.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>9</td><tr style='background-color:#ffffff'><td><b>10:00 am</b></td><td><a href='listsession.php?sd=2012-09-13&st=10:00:00'><span 	style='font-size:12px'>prediction</span></a></td><td>1</td><td><span 	style='font-size:12px'>You will complete several personality surveys on a desktop computer and complete a short exercise in which you edit a paragraph in microsoft word.  The study should take about 30 minutes.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>4</td><tr style='background-color:#fcead7'><td><b>10:15 am</b></td><td><a href='listsession.php?sd=2012-09-13&st=10:15:00'><span 	style='font-size:12px'>prediction</span></a></td><td>1</td><td><span 	style='font-size:12px'>You will complete several personality surveys on a desktop computer and complete a short exercise in which you edit a paragraph in microsoft word.  The study should take about 30 minutes.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>10</td><tr style='background-color:#ffffff'><td><b>10:30 am</b></td><td><a href='listsession.php?sd=2012-09-13&st=10:30:00'><span 	style='font-size:12px'>prediction</span></a></td><td>1</td><td><span 	style='font-size:12px'>You will complete several personality surveys on a desktop computer and complete a short exercise in which you edit a paragraph in microsoft word.  The study should take about 30 minutes.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>9</td><tr style='background-color:#fcead7'><td><b>10:45 am</b></td><td><a href='listsession.php?sd=2012-09-13&st=10:45:00'><span 	style='font-size:12px'>prediction</span></a></td><td>1</td><td><span 	style='font-size:12px'>You will complete several personality surveys on a desktop computer and complete a short exercise in which you edit a paragraph in microsoft word.  The study should take about 30 minutes.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>1</td><tr style='background-color:#ffffff'><td><b>11:00 am</b></td><td><a href='listsession.php?sd=2012-09-13&st=11:00:00'><span 	style='font-size:12px'>Psychological Science</span></a></td><td>1</td><td><span 	style='font-size:12px'>You are invited to participate in an experiment on various aspects of social psychology. In general, you will be asked to answer questions about yourself and your personality, and you will complete various tasks related to creativity and cognitive abilities. All in all, this experiment should take 50 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>4</td><tr style='background-color:#fcead7'><td><b>11:30 am</b></td><td><a href='listsession.php?sd=2012-09-13&st=11:30:00'><span 	style='font-size:12px'>Allocation in a Public Goods Game</span></a></td><td>1</td><td><span 	style='font-size:12px'>We are studying how people allocate points in a computerized economic game, and how people react to the allocations of other players. Participants play this game via a computer display and do not know the identities of other players. </span></td><td><span 	style='font-size:12px'><br/></span></td><td>0</td><tr style='background-color:#ffffff'><td></td><td><a href='listsession.php?sd=2012-09-13&st=11:30:00'><span style='font-size:12px'>Categorization and Memory</span></a></td><td>1</td><td><span style='font-size:12px'>Subjects learn to categorize and remember colors.</span></td><td><span 	style='font-size:12px'>Normal color vision.<br/><b>Categorization and Memory</b>:Proper color vision required</span></td><td>0</td></td><tr style='background-color:#fcead7'><td></td><td><a href='listsession.php?sd=2012-09-13&st=11:30:00'><span style='font-size:12px'>Categorizing Math Problems</span></a></td><td>1</td><td><span style='font-size:12px'>You'll learn about different types of math problems and then categorize problems according to their type. The problems all come from probability & statistics, so the experiment could help you get a better handle on ideas from Finite Math and / or Introductory Statistics.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>0</td></td><tr style='background-color:#ffffff'><td><b>12:00 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=12:00:00'><span 	style='font-size:12px'>Psychological Science</span></a></td><td>1</td><td><span 	style='font-size:12px'>You are invited to participate in an experiment on various aspects of social psychology. In general, you will be asked to answer questions about yourself and your personality, and you will complete various tasks related to creativity and cognitive abilities. All in all, this experiment should take 50 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>5</td><tr style='background-color:#fcead7'><td></td><td><a href='listsession.php?sd=2012-09-13&st=12:00:00'><span style='font-size:12px'>Third Party Ratings of Attraction</span></a></td><td>1</td><td><span style='font-size:12px'>View a series of videos of real speed-dates, and judge whether daters are interested in each other. Judge the attractiveness of faces in photographs. Answer questions about yourself, including personality, relationship history, sexual preferences. Answers are confidential. </span></td><td><span 	style='font-size:12px'>18 years or older<br/><b>Third Party Ratings of Attraction</b>:This experiment is NOT RUN in the Psychology Building. Hillcrest is 5 minutes away down 10th Street. Directions can be found at:
http://www.indiana.edu/~abcwest/pmwiki/pmwiki.php?n=Main.Contact  
</span></td><td>3</td></td><tr style='background-color:#ffffff'><td><b>12:15 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=12:15:00'><span 	style='font-size:12px'>Allocation in a Public Goods Game</span></a></td><td>1</td><td><span 	style='font-size:12px'>We are studying how people allocate points in a computerized economic game, and how people react to the allocations of other players. Participants play this game via a computer display and do not know the identities of other players. </span></td><td><span 	style='font-size:12px'><br/></span></td><td>1</td><tr style='background-color:#fcead7'><td><b>12:30 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=12:30:00'><span 	style='font-size:12px'>Categorizing Math Problems</span></a></td><td>1</td><td><span 	style='font-size:12px'>You'll learn about different types of math problems and then categorize problems according to their type. The problems all come from probability & statistics, so the experiment could help you get a better handle on ideas from Finite Math and / or Introductory Statistics.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>0</td><tr style='background-color:#ffffff'><td></td><td><a href='listsession.php?sd=2012-09-13&st=12:30:00'><span style='font-size:12px'>Third Party Ratings of Attraction</span></a></td><td>1</td><td><span style='font-size:12px'>View a series of videos of real speed-dates, and judge whether daters are interested in each other. Judge the attractiveness of faces in photographs. Answer questions about yourself, including personality, relationship history, sexual preferences. Answers are confidential. </span></td><td><span 	style='font-size:12px'>18 years or older<br/><b>Third Party Ratings of Attraction</b>:This experiment is NOT RUN in the Psychology Building. Hillcrest is 5 minutes away down 10th Street. Directions can be found at:
http://www.indiana.edu/~abcwest/pmwiki/pmwiki.php?n=Main.Contact  
</span></td><td>4</td></td><tr style='background-color:#fcead7'><td><b>1:00 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=13:00:00'><span 	style='font-size:12px'>Allocation in a Public Goods Game</span></a></td><td>1</td><td><span 	style='font-size:12px'>We are studying how people allocate points in a computerized economic game, and how people react to the allocations of other players. Participants play this game via a computer display and do not know the identities of other players. </span></td><td><span 	style='font-size:12px'><br/></span></td><td>0</td><tr style='background-color:#ffffff'><td></td><td><a href='listsession.php?sd=2012-09-13&st=13:00:00'><span style='font-size:12px'>Human Cognition</span></a></td><td>1</td><td><span style='font-size:12px'>You are invited to participate in an experiment on various challenging cognitive tasks. In general, you will be asked to complete a series of activities, such as a hand-grip exercise, a number puzzle, and a word challenge, while also answering several questions about yourself and your personality. In general, this experiment will take around 40 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>0</td></td><tr style='background-color:#fcead7'><td></td><td><a href='listsession.php?sd=2012-09-13&st=13:00:00'><span style='font-size:12px'>Third Party Ratings of Attraction</span></a></td><td>1</td><td><span style='font-size:12px'>View a series of videos of real speed-dates, and judge whether daters are interested in each other. Judge the attractiveness of faces in photographs. Answer questions about yourself, including personality, relationship history, sexual preferences. Answers are confidential. </span></td><td><span 	style='font-size:12px'>18 years or older<br/><b>Third Party Ratings of Attraction</b>:This experiment is NOT RUN in the Psychology Building. Hillcrest is 5 minutes away down 10th Street. Directions can be found at:
http://www.indiana.edu/~abcwest/pmwiki/pmwiki.php?n=Main.Contact  
</span></td><td>4</td></td><tr style='background-color:#ffffff'><td><b>1:15 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=13:15:00'><span 	style='font-size:12px'>Human Cognition</span></a></td><td>1</td><td><span 	style='font-size:12px'>You are invited to participate in an experiment on various challenging cognitive tasks. In general, you will be asked to complete a series of activities, such as a hand-grip exercise, a number puzzle, and a word challenge, while also answering several questions about yourself and your personality. In general, this experiment will take around 40 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>0</td><tr style='background-color:#fcead7'><td><b>1:30 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=13:30:00'><span 	style='font-size:12px'>Human Cognition</span></a></td><td>1</td><td><span 	style='font-size:12px'>You are invited to participate in an experiment on various challenging cognitive tasks. In general, you will be asked to complete a series of activities, such as a hand-grip exercise, a number puzzle, and a word challenge, while also answering several questions about yourself and your personality. In general, this experiment will take around 40 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>0</td><tr style='background-color:#ffffff'><td></td><td><a href='listsession.php?sd=2012-09-13&st=13:30:00'><span style='font-size:12px'>Thinking about Probabilities</span></a></td><td>1</td><td><span style='font-size:12px'>Subjects will be given simple stories about probabilities, and asked to reason about them.  They will then be given a short tutorial about probability.  The experiment explores the effectiveness of different instruction methods.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>2</td></td><tr style='background-color:#fcead7'><td></td><td><a href='listsession.php?sd=2012-09-13&st=13:30:00'><span style='font-size:12px'>Third Party Ratings of Attraction</span></a></td><td>1</td><td><span style='font-size:12px'>View a series of videos of real speed-dates, and judge whether daters are interested in each other. Judge the attractiveness of faces in photographs. Answer questions about yourself, including personality, relationship history, sexual preferences. Answers are confidential. </span></td><td><span 	style='font-size:12px'>18 years or older<br/><b>Third Party Ratings of Attraction</b>:This experiment is NOT RUN in the Psychology Building. Hillcrest is 5 minutes away down 10th Street. Directions can be found at:
http://www.indiana.edu/~abcwest/pmwiki/pmwiki.php?n=Main.Contact  
</span></td><td>4</td></td><tr style='background-color:#ffffff'><td><b>1:45 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=13:45:00'><span 	style='font-size:12px'>Human Cognition</span></a></td><td>1</td><td><span 	style='font-size:12px'>You are invited to participate in an experiment on various challenging cognitive tasks. In general, you will be asked to complete a series of activities, such as a hand-grip exercise, a number puzzle, and a word challenge, while also answering several questions about yourself and your personality. In general, this experiment will take around 40 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>0</td><tr style='background-color:#fcead7'><td><b>2:00 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=14:00:00'><span 	style='font-size:12px'>Early Word Learning</span></a></td><td>1</td><td><span 	style='font-size:12px'>Participants will complete a computer task where they will presented with words and objects and have to respond to these words and objects.</span></td><td><span 	style='font-size:12px'>Little to no experience in a second language<br/></span></td><td>0</td><tr style='background-color:#ffffff'><td></td><td><a href='listsession.php?sd=2012-09-13&st=14:00:00'><span style='font-size:12px'>Human Cognition</span></a></td><td>1</td><td><span style='font-size:12px'>You are invited to participate in an experiment on various challenging cognitive tasks. In general, you will be asked to complete a series of activities, such as a hand-grip exercise, a number puzzle, and a word challenge, while also answering several questions about yourself and your personality. In general, this experiment will take around 40 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>0</td></td><tr style='background-color:#fcead7'><td></td><td><a href='listsession.php?sd=2012-09-13&st=14:00:00'><span style='font-size:12px'>Third Party Ratings of Attraction</span></a></td><td>1</td><td><span style='font-size:12px'>View a series of videos of real speed-dates, and judge whether daters are interested in each other. Judge the attractiveness of faces in photographs. Answer questions about yourself, including personality, relationship history, sexual preferences. Answers are confidential. </span></td><td><span 	style='font-size:12px'>18 years or older<br/><b>Third Party Ratings of Attraction</b>:This experiment is NOT RUN in the Psychology Building. Hillcrest is 5 minutes away down 10th Street. Directions can be found at:
http://www.indiana.edu/~abcwest/pmwiki/pmwiki.php?n=Main.Contact  
</span></td><td>3</td></td><tr style='background-color:#ffffff'><td><b>2:15 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=14:15:00'><span 	style='font-size:12px'>Human Cognition</span></a></td><td>1</td><td><span 	style='font-size:12px'>You are invited to participate in an experiment on various challenging cognitive tasks. In general, you will be asked to complete a series of activities, such as a hand-grip exercise, a number puzzle, and a word challenge, while also answering several questions about yourself and your personality. In general, this experiment will take around 40 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>0</td><tr style='background-color:#fcead7'><td><b>2:30 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=14:30:00'><span 	style='font-size:12px'>Thinking about Probabilities</span></a></td><td>1</td><td><span 	style='font-size:12px'>Subjects will be given simple stories about probabilities, and asked to reason about them.  They will then be given a short tutorial about probability.  The experiment explores the effectiveness of different instruction methods.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>3</td><tr style='background-color:#ffffff'><td></td><td><a href='listsession.php?sd=2012-09-13&st=14:30:00'><span style='font-size:12px'>Third Party Ratings of Attraction</span></a></td><td>1</td><td><span style='font-size:12px'>View a series of videos of real speed-dates, and judge whether daters are interested in each other. Judge the attractiveness of faces in photographs. Answer questions about yourself, including personality, relationship history, sexual preferences. Answers are confidential. </span></td><td><span 	style='font-size:12px'>18 years or older<br/><b>Third Party Ratings of Attraction</b>:This experiment is NOT RUN in the Psychology Building. Hillcrest is 5 minutes away down 10th Street. Directions can be found at:
http://www.indiana.edu/~abcwest/pmwiki/pmwiki.php?n=Main.Contact  
</span></td><td>4</td></td><tr style='background-color:#fcead7'><td><b>3:30 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=15:30:00'><span 	style='font-size:12px'>Categorization and Memory</span></a></td><td>1</td><td><span 	style='font-size:12px'>Subjects learn to categorize and remember colors.</span></td><td><span 	style='font-size:12px'>Normal color vision.<br/><b>Categorization and Memory</b>:Proper color vision required</span></td><td>0</td><tr style='background-color:#ffffff'><td></td><td><a href='listsession.php?sd=2012-09-13&st=15:30:00'><span style='font-size:12px'>Thinking about Probabilities</span></a></td><td>1</td><td><span style='font-size:12px'>Subjects will be given simple stories about probabilities, and asked to reason about them.  They will then be given a short tutorial about probability.  The experiment explores the effectiveness of different instruction methods.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>2</td></td><tr style='background-color:#fcead7'><td><b>4:00 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=16:00:00'><span 	style='font-size:12px'>Human Cognition</span></a></td><td>1</td><td><span 	style='font-size:12px'>You are invited to participate in an experiment on various challenging cognitive tasks. In general, you will be asked to complete a series of activities, such as a hand-grip exercise, a number puzzle, and a word challenge, while also answering several questions about yourself and your personality. In general, this experiment will take around 40 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>0</td><tr style='background-color:#ffffff'><td><b>4:10 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=16:10:00'><span 	style='font-size:12px'>Human Cognition</span></a></td><td>1</td><td><span 	style='font-size:12px'>You are invited to participate in an experiment on various challenging cognitive tasks. In general, you will be asked to complete a series of activities, such as a hand-grip exercise, a number puzzle, and a word challenge, while also answering several questions about yourself and your personality. In general, this experiment will take around 40 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>0</td><tr style='background-color:#fcead7'><td><b>4:20 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=16:20:00'><span 	style='font-size:12px'>Human Cognition</span></a></td><td>1</td><td><span 	style='font-size:12px'>You are invited to participate in an experiment on various challenging cognitive tasks. In general, you will be asked to complete a series of activities, such as a hand-grip exercise, a number puzzle, and a word challenge, while also answering several questions about yourself and your personality. In general, this experiment will take around 40 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>0</td><tr style='background-color:#ffffff'><td><b>4:30 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=16:30:00'><span 	style='font-size:12px'>Human Cognition</span></a></td><td>1</td><td><span 	style='font-size:12px'>You are invited to participate in an experiment on various challenging cognitive tasks. In general, you will be asked to complete a series of activities, such as a hand-grip exercise, a number puzzle, and a word challenge, while also answering several questions about yourself and your personality. In general, this experiment will take around 40 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>1</td><tr style='background-color:#fcead7'><td><b>4:40 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=16:40:00'><span 	style='font-size:12px'>Human Cognition</span></a></td><td>1</td><td><span 	style='font-size:12px'>You are invited to participate in an experiment on various challenging cognitive tasks. In general, you will be asked to complete a series of activities, such as a hand-grip exercise, a number puzzle, and a word challenge, while also answering several questions about yourself and your personality. In general, this experiment will take around 40 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>1</td><tr style='background-color:#ffffff'><td><b>4:50 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=16:50:00'><span 	style='font-size:12px'>Human Cognition</span></a></td><td>1</td><td><span 	style='font-size:12px'>You are invited to participate in an experiment on various challenging cognitive tasks. In general, you will be asked to complete a series of activities, such as a hand-grip exercise, a number puzzle, and a word challenge, while also answering several questions about yourself and your personality. In general, this experiment will take around 40 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>1</td><tr style='background-color:#fcead7'><td><b>5:00 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=17:00:00'><span 	style='font-size:12px'>Human Cognition</span></a></td><td>1</td><td><span 	style='font-size:12px'>You are invited to participate in an experiment on various challenging cognitive tasks. In general, you will be asked to complete a series of activities, such as a hand-grip exercise, a number puzzle, and a word challenge, while also answering several questions about yourself and your personality. In general, this experiment will take around 40 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>0</td><tr style='background-color:#ffffff'><td><b>5:10 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=17:10:00'><span 	style='font-size:12px'>Human Cognition</span></a></td><td>1</td><td><span 	style='font-size:12px'>You are invited to participate in an experiment on various challenging cognitive tasks. In general, you will be asked to complete a series of activities, such as a hand-grip exercise, a number puzzle, and a word challenge, while also answering several questions about yourself and your personality. In general, this experiment will take around 40 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>0</td><tr style='background-color:#fcead7'><td><b>5:20 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=17:20:00'><span 	style='font-size:12px'>Human Cognition</span></a></td><td>1</td><td><span 	style='font-size:12px'>You are invited to participate in an experiment on various challenging cognitive tasks. In general, you will be asked to complete a series of activities, such as a hand-grip exercise, a number puzzle, and a word challenge, while also answering several questions about yourself and your personality. In general, this experiment will take around 40 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>0</td><tr style='background-color:#ffffff'><td><b>5:30 pm</b></td><td><a href='listsession.php?sd=2012-09-13&st=17:30:00'><span 	style='font-size:12px'>Human Cognition</span></a></td><td>1</td><td><span 	style='font-size:12px'>You are invited to participate in an experiment on various challenging cognitive tasks. In general, you will be asked to complete a series of activities, such as a hand-grip exercise, a number puzzle, and a word challenge, while also answering several questions about yourself and your personality. In general, this experiment will take around 40 minutes to complete.</span></td><td><span 	style='font-size:12px'><br/></span></td><td>1</td></tr></table></td></tr></table>


</div> <!-- end content -->

<div class="sidebar">
<h3>Menu</h3>
  <a href="index.php">Home</a><br/><br/>
  <a href="profile.php">Update Profile</a><br/><br/>
  <a href="showdaily.php">Experiment Sign-Up</a><br/><br/>
  <a href="listcredits.php">Lookup Credit Totals</a><br/><br/>
  <a href="showregistrations.php">Lookup or Cancel Reservations</a><br/><br/>
  <a href="listsurveys.php">List of Online Surveys</a><br/><br/>
  <a href="instructions.htm" target="_blank">Instructions</a><br/><br/>
</ul>

dubeasle logged in
</div> <!-- end sidebar -->

<!-- need a non-floating element to properly calculate container height -->
<div class="clear"></div>

</div> <!-- end main -->

<p class="footer">
Last updated:
<script language="JavaScript">
var current_date = new Date ( );
document.write(current_date.getMonth()+1 + "/" + current_date.getFullYear()  );
</script>
|| Comments:  <a href="http://bl-psy-appsrv.ads.iu.edu:8080/domail1.asp?t=psych" target="_blank">Email Psychology Webmaster</a>
 ||  <a href="http://www.indiana.edu/copyright.html" target="_blank">Copyright &copy; 
<script type="text/javascript">
				<!--
				var current_date = new Date ( );
				document.write ( " " + current_date.getFullYear() );
				// -->
			</script>
</a> 
The Trustees of  <a href="http://www.indiana.edu" target="_blank">Indiana University</a> 
||  <a href="http://www.indiana.edu/copyright_complaints.shtml" target="_blank">Copyright Complaints </a>


</p>

</div> <!-- end wrapper -->
</body>
</html>
