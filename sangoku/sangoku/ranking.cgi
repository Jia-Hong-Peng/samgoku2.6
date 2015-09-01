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
if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("∏T§Ó®œ•Œ™Ω±µ∏ÙÆ|°C"); }
if($mode eq 'C_RAN') { &C_RAN; }
else{&RANKING;}


#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#°@°@°@°@ ∞—•[™Ã¶W≥ÊOPEN°@°@ °@°@#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub RANKING {

	&SERVER_STOP;

	open(IN,"$CHARA_DATA");
	@DL_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_LIST") or &ERR2('•¥§£∂}§Â•Û°C');
	@COU_DATA = <IN>;
	close(IN);
	$country_no=0;

	foreach(@COU_DATA){
		($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
		$cou_name[$country_no]="$xname";
		$c[$country_no]=0;
		$c_no[$country_no]=$xcid;
		$c_king[$country_no]=$xking;
		($xgunshi,$xdai)= split(/,/,$xsub);
		$c_gun[$country_no]=$xgunshi;
		$c_dai[$country_no]=$xdai;
		$country_no++;
	}

	open(IN,"$TOWN_LIST");
	@T_LIST = <IN>;
	close(IN);
	$town_c0=0;$town_c1=0;$town_c2=0;$town_c3=0;
	$l=0;
	foreach(@T_LIST){
		($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$z[0],$z[1],$z[2],$z[3])=split(/<>/);
		$TOWN_NAME[$l]="$zname";
		for($p=0;$p<$country_no;$p++){
			if($zcon eq "$c_no[$p]"){$town_c[$p]++;$mes[$p].="$zname ";}
		}
		$l++;
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
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	@tmp = map {(split /<>/)[14]} @CL_DATA;
	@CL_DATA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];
	$num = @CL_DATA;
	$i=0;
	$date = time;

	foreach(@CL_DATA) {
	($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		$s_num = int($kclass / $LANK);
		if($s_num > 20){$s_num = 20;}

		$chit=0;
		for($j=0;$j<$country_no;$j++){
			if($kcon eq "$c_no[$j]"){
				$chit=1;
				if($kid eq "$c_king[$j]"){
					$c_k_name[$j] = $kname;
				}
				if($kid eq "$c_gun[$j]"){
					$c_g_name[$j] = $kname;
				}
				if($kid eq "$c_dai[$j]"){
					$c_d_name[$j] = $kname;
				}
				if($c[$j] <= 10 && $kcon ne 0){
				$ldate = $DEL_TURN - $ksub2;
				if($ldate <= 0){
					$rm = "<font color=red>ßR∞£πÔ∂H</font>";
				}else{
					$rm = "<font color=blue>$ldate</font>";
				}
				$list[$j] .= "<TR><TD><img src=$IMG/$kchara.gif></TD><TD>$kname</TD><TD>$kstr</TD><TD>$kint</TD><TD>$klea</TD><TD>$ksol</TD><TD>$LANK[$s_num]</TD><TD>$rm¶^¶X</TD></TR>";
				}else{
					$lista[$j] .= "$kname($LANK[$s_num]) ";
				}
				$c[$j]++;
			}
		}

		if(!$chit){
				$list_etc .= "$kname ";
		}
	}

	&HEADER;
	$l_rank = "<TR><TD></TD><TH>¶W¶r</TH><TH>™Z§O</TH><TH>™æ§O</TH><TH>≤Œ≤v§O</TH><TH>ßL§hº∆</TH><TH>∂•Ø≈</TH><TH>ßR∞£</TH></TR>";

	print <<"EOM";
<div align="center"><TABLE WIDTH="70%" height=100% bgcolor=$TABLE_C>
  <TBODY>
    <TR>
      <TD BGCOLOR=$TD_C1 WIDTH=100% height=5><div align="center"><font size=4>°’°’<B> Å@ - RANKING - Å@ </B>°÷°÷</font></div></TD>
    </TR>
    <TR>
      <TD bgcolor=$TD_C4><CENTER>
<BR>
EOM

	$c_c=0;
	$c_i=0;
	foreach(@COU_DATA){
		($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
		if($xking ne "" && $c_k_name[$c_c] eq ""){
			open(IN,"./charalog/main/$xking.cgi");
			@CN_DATA = <IN>;
			close(IN);
			($lid,$lpass,$lname) = split(/<>/,$CN_DATA[0]);
			$c_k_name[$c_c] = "$lname";
		}
print<<"EOM";
<TABLE bgcolor=$ELE_BG[$xele] width=80%><TBODY><TR><TD colspan=5 bgcolor=$ELE_BG[$xele] align=center><font color=$ELE_C[$xele] size=4><B>$xname</font></TD></TR><TR><TH bgcolor=$ELE_C[$xele]><font color=$ELE_BG[$xele]>ßg•D</TH><TH bgcolor=FFFFFF><font size=3 color=$ELE_BG[$xele]>$c_k_name[$c_c]</TH><TD bgcolor=$ELE_C[$xele]><font color=$ELE_BG[$xele]>™Z±Nº∆</TD><TD bgcolor=$ELE_C[$xele]><font color=$ELE_BG[$xele]> $c[$c_c] ¶W</TD><TD bgcolor=$ELE_C[$xele]><a href=./$FILE_RANK?mode=C_RAN&con_no=$xcid>™Z±N§@ƒ˝</a></TD></TR><TR><TH bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>≠xÆv</TH><TH bgcolor=$ELE_C[$xele]><font size=2 color=$ELE_BG[$xele]>$c_g_name[$c_c]</TH><TH bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>§j±N≠x</TH><TH colspan=2 bgcolor=$ELE_C[$xele]><font size=2 color=$ELE_BG[$xele]>$c_d_name[$c_c]</TH></TR><TR><TD bgcolor=$ELE_C[$xele]><font color=$ELE_BG[$xele]>§‰∞t≥£•´º∆</TD><TD colspan=4 bgcolor=$ELE_C[$xele]><font color=$ELE_BG[$xele]>$town_c[$c_c]≥£•´($mes[$c_c])</TD></TR></TBODY></TABLE><BR>
      <TABLE bgcolor=$ELE_BG[$xele] width=80% border="0">
        <TBODY bgcolor=$ELE_C[$xele]>
$l_rank $list[$c_i] 
         </TR>
		<TR><TD bgcolor=$ELE_C[$xele] align=center colspan=20><font color=$ELE_BG[$xele]>$lista[$c_i]
		</TD></TR>
        </TBODY>
      </TABLE><br><br><br><br><br>
EOM
		$c_c++;
		$c_i++;
	}

print <<"EOM";
<TABLE bgcolor=$ELE_BG[0] width=80%><TBODY><TR><TD colspan=5 bgcolor=$ELE_BG[0] align=center><font color=$ELE_C[0] size=4><B>µL©“ƒ›∞Í</font></TD></TR><TR><TD align=center bgcolor=$ELE_C[0]><a href=./$FILE_RANK?mode=C_RAN&con_no=0>¶b≥•™Z±N§@ƒ˝</a></TD></TR></TBODY></TABLE><BR>
      <TABLE width=80% bgcolor=$ELE_BG[0] border="0">
        <TBODY bgcolor=$ELE_C[0]>
		<TR><TD bgcolor=$ELE_C[0] align=center><font color=$ELE_BG[0]>$list_etc
		</TD></TR>
        </TBODY>
      </TABLE><br><br><br><br><br>
<p>≤{¶b¡`§H§f $num ¶W
<form action="$FILE_TOP" method="post">
<input type=submit value="™¶^"></form>

      </TD>
    </TR>
  </TBODY>
</TABLE>
EOM

	&FOOTER;

	exit;
}


sub C_RAN{

	&SERVER_STOP;

	$C_NEXT_NUM = 100;

	open(IN,"$CHARA_DATA");
	@DL_DATA = <IN>;
	close(IN);
	$date = time;

	open(IN,"$COUNTRY_LIST") or &ERR2('•¥§£∂}§Â•Û°C');
	@COU_DATA = <IN>;
	close(IN);
	$country_no=0;
	foreach(@COU_DATA){
		($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
		$cou_name[$xcid]="$xname";
		$c[$country_no]=0;
		$c_no[$country_no]=$xcid;
		$c_king[$country_no]=$xking;
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
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	@tmp = map {(split /<>/)[14]} @CL_DATA;
	@CL_DATA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];
	$num = @CL_DATA;
	$i=0;

	if($in{'c_num'} eq ""){
		$c_num = 0;
	}else{
		$c_num = $in{'c_num'};
	}

		$j=0;
	if($in{'con_no'} ne "0"){
		foreach(@CL_DATA) {
	($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		$s_num = int($kclass / $LANK);
		if($s_num > 20){$s_num = 20;}

		$chit=0;
		for($j=0;$j<$country_no;$j++){
			if($kcon eq "$c_no[$j]"){
				
			}
			if($kcon eq "$in{'con_no'}"){
			$chit=1;
			if($kid eq "$c_king[$j]"){
				$c_k_name[$j] = $kname;
			}
			$ldate = $DEL_TURN - $ksub2;
			if($ldate <= 0){
				$rm = "<font color=red>ßR∞£πÔ∂H</font>";
			}else{
				$rm = "<font color=blue>$ldate</font>";
			}
			$list[$j] .= "<TR><TD><img src=$IMG/$kchara.gif></TD><TD>$kname</TD><TD>$kstr</TD><TD>$kint</TD><TD>$klea</TD><TD>$ksol</TD><TD>$LAMK[$s_num]</TD><TD>$rm¶^¶X</TD></TR>";
			$c[$j]++;
			}

			}
		}
	}else{
		foreach(@CL_DATA) {
	($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
			$s_num = int($kclass / $LANK);
			if($s_num > 20){$s_num = 20;}

			$chit=0;
			for($j=0;$j<$country_no;$j++){
				if($kcon eq "$c_no[$j]"){
				$chit=1;
				last;
				}
			}
			$ldate = $DEL_TURN - $ksub2;
			if($ldate <= 0){
				$rm = "<font color=red>ßR∞£πÔ∞£</font>";
			}else{
				$rm = "<font color=blue>$ldate</font>";
			}

			if(!$chit){
			if($c[0] >= $c_num && $c[0] < $c_num + $C_NEXT_NUM){
			$list[0] .= "<TR><TD><img src=$IMG/$kchara.gif></TD><TD>$kname</TD><TD>$kstr</TD><TD>$kint</TD><TD>$klea</TD><TD>$ksol</TD><TD></TD><TD>$rm¶^¶X</TD></TR>";
			}
				$c[0]++;
			}
		}
	}

	&HEADER;

	$l_rank = "<TR><TD></TD><TH>¶W¶r</TH><TH>™Z§O</TH><TH>™æ§O</TH><TH>≤Œ≤v§O</TH><TH>ßL§hº∆</TH><TH>∂•Ø≈</TH><TH>ßR∞£</TH></TR>";

	print <<"EOM";
<div align="center"><TABLE WIDTH="70%" height=100% bgcolor=$TABLE_C>
  <TBODY>
    <TR>
      <TD BGCOLOR=$TD_C1 WIDTH=100% height=5><div align="center"><font size=4>°’°’<B> Å@ - RANKING - Å@ </B>°÷°÷</font></div></TD>
    </TR>
    <TR>
      <TD bgcolor=$TD_C4><CENTER>
<BR>
EOM

	$c_c=0;
	if($in{'con_no'} ne "0"){

		foreach(@COU_DATA){
		($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
			if($xcid eq $in{'con_no'}){
			if($xking ne "" && $c_k_name[$c_c] eq ""){
				open(IN,"./charalog/main/$xking.cgi") or &ERR2('®S∂}§Â•Û°Cerr no :main_chara');
				@CN_DATA = <IN>;
				close(IN);
				($lid,$lpass,$lname) = split(/<>/,$CN_DATA[0]);
				$c_k_name[$c_c] = "$lname";
			}
	print<<"EOM";
	<TABLE bgcolor=$ELE_BG[$xele] width=80%><TBODY><TR><TD colspan=4 bgcolor=$ELE_BG[$xele] align=center><font color=$ELE_C[$xele] size=4><B>$xname</font></TD></TR><TR><TH bgcolor=$ELE_C[$xele]><font color=$ELE_BG[$xele]>ßg•D</TH><TH bgcolor=FFFFFF><font size=3 color=$ELE_BG[$xele]>$c_k_name[$c_c]</TH><TD bgcolor=$ELE_C[$xele]><div align="center"><font color=$ELE_BG[$xele]>™Z±Nº∆</div></TD><TD bgcolor=$ELE_C[$xele]><div align="center"><font color=$ELE_BG[$xele]> $c[$c_c] ¶W</div></TD></TR></TBODY></TABLE><BR>
	      <TABLE bgcolor=$ELE_BG[$xele] width=80% border="0">
	        <TBODY bgcolor=$ELE_C[$xele]>
	$l_rank $list[$c_c] 
	         </TR>
			<TR><TD bgcolor=$ELE_C[$xxele] align=center colspan=20><font color=$ELE_BG[$xxele]>$lista[0]
			</TD></TR>
	        </TBODY>
	      </TABLE><br><br><br><br><br>
EOM
			$c_c++;
			}
		}

	}else{

	$xele=0;

	print<<"EOM";
	<TABLE bgcolor=$ELE_BG[$xxele] width=80%><TBODY><TR><TD colspan=2 bgcolor=$ELE_BG[$xele] align=center><font color=$ELE_C[$xele] size=4><B>µL©“ƒ›</font></TD></TR><TR><TD bgcolor=$ELE_C[$xele]><div align="center"><font color=$ELE_BG[$xele]>™Z±Nº∆</div></TD><TD bgcolor=$ELE_C[$xele]><div align="center"><font color=$ELE_BG[$xele]> $c[$c_c] ¶W</div></TD></TR></TBODY></TABLE><BR>
	      <TABLE bgcolor=$ELE_BG[$xele] width=80% border="0">
	        <TBODY bgcolor=$ELE_C[$xele]>
	$l_rank $list[$c_c] 
	         </TR>
	        </TBODY>
	      </TABLE></div><br><br><br><br><br>
EOM
	}

	$q=0;
	for($p=0;$p<$c[0];$p+=$C_NEXT_NUM){
		$next_mes .= "\[<a href=./$FILE_RANK?mode=C_RAN&con_no=$in{'con_no'}&c_num=$p>$q</a>\] ";
		$q++;
	}
	
print <<"EOM";
$next_mes
<form action="$FILE_RANK" method="post">
<input type=submit value="RANKING TOP"></form>

      </TD>
    </TR>
  </TBODY>
</TABLE></div><center>
EOM

	&FOOTER;

	exit;

}
