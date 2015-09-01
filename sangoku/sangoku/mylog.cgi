#!/usr/bin/perl

#################################################################
#°@°ißK≥d±¯¥⁄°j°@°@°@°@°@°@°@°@°@°@°@°@°@°@°@°@°@°@     °@°@°@°@#
#°@≥o≠”µ{¶°¨OßK∂O≥n•Û°C¶p®œ•Œ≥o≠”µ{¶°°@°@°@°@°@°@°@°@     °@°@°@#
#°@¶”∑l•¢™Ãµ{¶°ß@™Ã±N§£©”æ·§@§¡§ß≥d•Ù°C°@°@°@°@°@°@°@     °@°@°@#
#°@¶≥√ˆ≥]∏m™∫∞›√DΩ–®Ï•ªØ∏™∫¥¶•‹™O∞QΩ◊°C°@°@°@°@°@°@°@°@     °@°@#
#°@•Ù¶Û∞›√D§£±µ®¸∂l•Û¨d∏ﬂ°C°@°@°@°@°@°@°@°@°@°@°@°@°@°@     °@  #
#################################################################

#require 'jcode.pl';
require './withlove_sgkini/index.ini';
require 'suport.pl';

if($MENTE) { &ERR("∫˚≈@§§°CΩ–µy´·¶A∏’°C"); }
&DECODE;
&TOP;

#_/_/_/_/_/_/_/_/_/#
#_/    TOPµe≠±   _/#
#_/_/_/_/_/_/_/_/_/#

sub TOP {

	&CHARA_MAIN_OPEN;
	open(IN,"./charalog/log/$kid.cgi");
	@LOG_DATA = <IN>;
	close(IN);
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);

	$p=0;
	foreach(@LOG_DATA){
		$log_list .= "<font color=navy>°¥</font>$LOG_DATA[$p]<BR>";$p++;
	}

	opendir(dirlist,"./charalog/main");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"./charalog/main/$file")){
				&ERR2("•¥§£∂}§Â•Û°I");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);



	$list = "<TR><TD></TD><TH>¶W¶r</TH><TH>™Z§O</TH><TH>™æ§O</TH><TH>≤Œ≤v§O</TH><TH>ßL§hº∆</TH><TH>∞Í¶W</TH><TH>´¸•O</TH></TR>";
	$num=0;
	foreach(@CL_DATA){
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/);
		if($epos eq $kpos){
			$num++;
			$com_list = "";
			if($kcon eq $econ){
				open(IN,"./charalog/command/$eid.cgi");
				@COM_DATA = <IN>;
				close(IN);
				for($i=0;$i<$MAX_COM;$i++){
					($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/,$COM_DATA[$i]);
					$no = $i+1;
					if($cid eq ""){
					$com_list .= "$no: - <BR>";
					}else{
					$com_list .= "$no:$cname<BR>";
					}
					if($i>=3){last;}
				}
			}
			if($num < 100){
			$list .= "<TR><TD><img src=$IMG/$echara.gif></TD><TD>$ename</TD><TD>$estr</TD><TD>$eint</TD><TD>$elea</TD><TD>$esol</TD><TD>$cou_name[$econ]</TD><TD>$com_list</TD></TR>";
			}
		}
	}
	&HEADER;
	print <<"EOM";
<CENTER>
<TABLE WIDTH="100%" height=100% cellpadding="0" cellspacing="0" border=0><tr><td align=center>
<B><font color="#FFFFFF">$zname∞±Ød™Ã ($num§H)</font></b>ÅF
<TABLE border=0 cellspacing=1 bgcolor=$TABLE_C>
    <TBODY bgcolor=FFFFFF>
$list
</TBODY></TABLE>

<TABLE border=0 cellspacing=1>
    <TBODY>
          <TR>
<TD><br>
<font color="#FFFFFF">$log_list</font>
<form action=\"$FILE_STATUS\" method=\"post\"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=STATUS><input type=submit value=\"™¶^≥£•´\"></form>
</TD></TR>
</TBODY></TABLE>


</TD></TR>
</TBODY></TABLE>

EOM

	&FOOTER;
	exit;

}

