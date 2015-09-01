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

if($MENTE) { &ERR2("∫˚≈@§§°CΩ–µy´·¶A∏’°C"); }
&DECODE;
#if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("∏T§Ó®œ•Œ™Ω±µ∏ÙÆ|°C"); }
&RANKING;


#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#°@ °@°@°@∞—•[™Ã¶W≥ÊOPEN°@°@ °@°@#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub RANKING {

	&SERVER_STOP;
	open(IN,"$COUNTRY_NO_LIST") or &ERR2('•¥§£∂}§Â•Û°C');
	@COU_DATA = <IN>;
	close(IN);
	$country_no=1;

	foreach(@COU_DATA){
		($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
		$cou_name[$country_no]="$xname";
		$country_no++;
	}

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR("•¥§£∂}§Â•Û°I");
			}
			@page = <page>;
			close(page);
			($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/,$page[0]);
			($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$ktec1,$ktec2,$ktec3,$kvsub1,$kvsub2,) = split(/,/,$ksub1);
			$lpoint = $kstr+$kint+$klea;
			push(@CL_DATA,"$kid<>$kpass<>$kname<>$kchara<>$kstr<>$kint<>$klea<>$kcha<>$ksol<>$kgat<>$kcon<>$kgold<>$krice<>$kcex<>$kclass<>$karm<>$kbook<>$kbank<>$ksub1<>$ksub2<>$kpos<>$kmes<>$khost<>$kdate<>$kmail<>$kos<>$lpoint<>$ksub2_ex<>\n");
		}
	}
	closedir(dirlist);



	@tmp = map {(split /<>/)[26]} @CL_DATA;
	@POINT = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;

	$best_list = "<TR><TD align=center>º–√D</TD><TD align=center>º∆≠»</TD><TD align=center colspan=2>¶W¶r</TD><TD align=center>∞Í</TD></TR>";

	$point_list = "<TR><TD align=center>¶W¶∏</TD><TD align=center>¡`¶X</TD><TD align=center>™Z§O</TD><TD align=center>™æ§O</TD><TD align=center>≤Œ≤v§O</TD><TD align=center colspan=2>¶W¶r</TD><TD align=center>∞Í</TD></TR>";
	foreach(@POINT){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "µL©“ƒ›";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><font color=FFFFFF>¡`¶X\Ø‡\§O No.1</TH><TH>$klpoint</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
			$point_list .= "<TR><TH><font color=blue>°i$i°j</font></TH><TH>$klpoint</TH><TD>$kstr</TD><TD>$kint</TD><TD>$klea</TD><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}else{
		$point_list .= "<TR><TD align=center>$i</TD><TH>$klpoint</TH><TD>$kstr</TD><TD>$kint</TD><TD>$klea</TD><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[4]} @CL_DATA;
	@STR = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$str_list = "<TR><TD align=center>¶W¶∏</TD><TD align=center>™Z§O</TD><TD align=center colspan=2>¶W¶r</TD><TD align=center>∞Í</TD></TR>";
	foreach(@STR){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "µL©“ƒ›";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><font color=FFFFFF>™Z§O No.1</TH><TH>$kstr</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		$str_list .= "<TR><TH><font color=blue>°i$i°j</font></TD><TH>$kstr</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}else{
		$str_list .= "<TR><TD align=center>$i</TD><TH>$kstr</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[5]} @CL_DATA;
	@INT = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$int_list = "<TR><TD align=center>¶W¶∏</TD><TD align=center>™æ§O</TD><TD align=center colspan=2>¶W¶r</TD><TD align=center>∞Í</TD></TR>";
	foreach(@INT){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "µL©“ƒ›";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><font color=FFFFFF>™æ§O No.1</TH><TH>$kint</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
			$int_list .= "<TR><TH><font color=blue>°i$i°j</TH><TH>$kint</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}else{
		$int_list .= "<TR><TD align=center>$i</TD><TH>$kint</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[6]} @CL_DATA;
	@LER = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$lea_list = "<TR><TD align=center>¶W¶∏</TD><TD align=center>≤Œ≤v§O</TD><TD align=center colspan=2>¶W¶r</TD><TD align=center>∞Í</TD></TR>";
	foreach(@LER){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "µL©“ƒ›";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
		$lea_list .= "<TR><TH><font color=blue>°i$i°j</font></TH><TH>$klea</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
			$best_list .= "<TR><TH bgcolor=664422><font color=FFFFFF>≤Œ≤v§O No.1</TH><TH>$klea</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}else{
		$lea_list .= "<TR><TD align=center>$i</TD><TH>$klea</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[7]} @CL_DATA;
	@CHA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$cha_list = "<TR><TD align=center>¶W¶∏</TD><TD align=center>§H±Ê</TD><TD align=center colspan=2>¶W¶r</TD><TD align=center>∞Í</TD></TR>";
	foreach(@CHA){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "µL©“ƒ›";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><font color=FFFFFF>§H±Ê No.1</TH><TH>$kcha</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		$cha_list .= "<TR><TH><font color=blue>°i$i°j</font></TH><TH>$kcha</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}else{
		$cha_list .= "<TR><TD align=center>$i</TD><TH>$kcha</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[11]} @CL_DATA;
	@GOLD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$gold_list = "<TR><TD align=center>¶W¶∏</TD><TD align=center>™˜</TD><TD align=center colspan=2>¶W¶r</TD><TD align=center>∞Í</TD></TR>";
	foreach(@GOLD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "µL©“ƒ›";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><font color=FFFFFF>©“´˘™˜ No.1</TH><TH>™˜°G$kgold</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		$gold_list .= "<TR><TH><font color=blue>°i$i°j</font></TH><TH>™˜°G$kgold</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}else{
		$gold_list .= "<TR><TD align=center>$i</TD><TH>™˜°G$kgold</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[12]} @CL_DATA;
	@RICE = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$rice_list = "<TR><TD align=center>¶W¶∏</TD><TD align=center>¶Ã</TD><TD align=center colspan=2>¶W¶r</TD><TD align=center>∞Í</TD></TR>";
	foreach(@RICE){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "µL©“ƒ›";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><font color=FFFFFF>¶Ã¶s∂q No.1</TH><TH>¶Ã°G$krice</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		$rice_list .= "<TR><TH><font color=blue>°i$i°j</font></TH><TH>¶Ã°G$krice</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}else{
		$rice_list .= "<TR><TD align=center>$i</TD><TH>¶Ã°G$krice</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[14]} @CL_DATA;
	@CLASS = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$class_list = "<TR><TD align=center>¶W¶∏</TD><TD align=center>∂•Ø≈≠»</TD><TD align=center colspan=2>¶W¶r</TD><TD align=center>∞Í</TD></TR>";
	foreach(@CLASS){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "µL©“ƒ›";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><font color=FFFFFF>∂•Ø≈≠» No.1</TH><TH>$kclass</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		$class_list .= "<TR><TH><font color=blue>°i$i°j</font></TH><TH>$kclass</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}else{
		$class_list .= "<TR><TD align=center>$i</TD><TH>$kclass</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	$dead_list = "<TR><TD align=center>¶W¶∏</TD><TD align=center>¿ª®Ï™Z±Nº∆</TD><TD align=center colspan=2>¶W¶r</TD><TD align=center>∞Í</TD></TR>";
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "µL©“ƒ›";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$best_list .= "<TR><TH bgcolor=664422><font color=FFFFFF>¿ª≠À™Z±N No.1</TH><TH>$knumêl</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		$dead_list .= "<TR><TH><font color=blue>°i$i°j</font></TH><TH>$knumêl</TH><TH><font color=AA0000>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}else{
		$dead_list .= "<TR><TD align=center>$i</TD><TH>$knumêl</TH><TH><font color=885522>$kname</TH><TD width=5><img src=$IMG/$kchara.gif></TD><TD align=center>$kcon_name</TD></TR>";
		}
		$i++;
		if($i>10){last;}
	}


	&HEADER;

	print <<"EOM";
$a
<CENTER><TABLE WIDTH="70%" height=100% bgcolor=$TABLE_C>
<TBODY><TR><TD BGCOLOR=$TD_C1 WIDTH=100% height=100% align=center>
<BR>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH bgcolor=#284422><font size=5 color=CCDDCC>- ¶W ±N §@ ƒ˝ -</font></TH></TR>
</TBODY></TABLE>

<BR><p>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>§T∞Í≠^∂Ø</font></TH></TR>
$best_list
</TBODY></TABLE>

<BR><p>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>§Q±j™Z™Ã</font></TH></TR>
$str_list
</TBODY></TABLE>

<BR><p>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>§Q§j¥º™Ã</font></TH></TR>
$int_list
</TBODY></TABLE>

<BR><p>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>§Q§j≤Œ´”</font></TH></TR>
$lea_list
</TBODY></TABLE>

<BR><p>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=8 bgcolor=#446644><font size=4 color=CCDDCC>§Q§j¶W±N</font></TH></TR>
$point_list
</TBODY></TABLE>

<BR><p>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>§Q§j≠^≥«</font></TH></TR>
$cha_list
</TBODY></TABLE>

<BR><p>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>§Q§j¥Iª®</font></TH></TR>
$gold_list
</TBODY></TABLE>

<BR><p>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>§Q§j¶Ã¶s</font></TH></TR>
$rice_list
</TBODY></TABLE>

<BR><p>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>§Q§j\•\\æ±</font></TH></TR>
$class_list
</TBODY></TABLE>

<BR><p>
<TABLE border=1 width=80% class=S3 cellspacing=0 CELLPADDING=0><TBODY>
<TR><TH colspan=5 bgcolor=#446644><font size=4 color=CCDDCC>§Q§jæ‘Ø´</font></TH></TR>
$dead_list
</TBODY></TABLE>



<form action="$FILE_TOP" method="post">
<input type=submit value="™¶^"></form>

      </TD>
    </TR>
  </TBODY>
</TABLE><br>
EOM

	&FOOTER;

	exit;
}


