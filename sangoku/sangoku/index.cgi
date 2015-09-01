#!/usr/bin/perl

#################################################################
#¡@¡i§K³d±ø´Ú¡j¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@     ¡@¡@¡@¡@#
#¡@³o­Óµ{¦¡¬O§K¶O³n¥ó¡C¦p¨Ï¥Î³o­Óµ{¦¡¡@¡@¡@¡@¡@¡@¡@¡@     ¡@¡@¡@#
#¡@¦Ó·l¥¢ªÌµ{¦¡§@ªÌ±N¤£©Ó¾á¤@¤Á¤§³d¥ô¡C¡@¡@¡@¡@¡@¡@¡@     ¡@¡@¡@#
#¡@¦³Ãö³]¸mªº°ÝÃD½Ð¨ì¥»¯¸ªº´¦¥ÜªO°Q½×¡C¡@¡@¡@¡@¡@¡@¡@¡@     ¡@¡@#
#¡@¥ô¦ó°ÝÃD¤£±µ¨ü¶l¥ó¬d¸ß¡C¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@     ¡@  #
#################################################################

#require 'jcode.pl';
require './withlove_sgkini/index.ini';
require 'suport.pl';

if($MENTE) { &ERR2("µ{§Ç®Ö¹ï¤@®É°±¤î¡C"); }
&DECODE;
&TOP;

#_/_/_/_/_/_/_/_/_/#
#_/    TOPµe­±   _/#
#_/_/_/_/_/_/_/_/_/#

sub TOP {

	$date = time();
	$month_read = "./withlove_sgklog/date_count.cgi";
	open(IN,"$month_read") or &ERR2('¥´¤£¶}¤å¥ó¡C');
	@MONTH_DATA = <IN>;
	close(IN);
	&TIME_DATA;

	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<5){$S_MES .= "<font color=008800>¡´ </font>$S_MOVE[$p]<BR>";$p++;}

	open(IN,"$MAP_LOG_LIST2");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<5){$D_MES .= "<font color=000088>¡´</font>$S_MOVE[$p]<BR>";$p++;}

	$hit = 0;
	@month_new=();

	($myear,$mmonth,$mtime) = split(/<>/,$MONTH_DATA[0]);
	$old_date = sprintf("%02d\¦~%02d\¤ë", $F_YEAR+$myear, $mmonth);

	if($ACT_LOG){
		$actfile = "./withlove_sgklog/act_log.cgi";
		open(IN,"$actfile");
		@ACT_DATA = <IN>;
		close(IN);
		($qsec,$qmin,$qhour,$qday) = localtime($date);
		$p=0;
		while($p<5){$A_MES .= "<font color=880000>¡´ </font>$ACT_DATA[$p]<BR>";$p++;}

		$ACT_MES = "<TD bgcolor=#EFE0C0 colspan=\"2\" width=80% height=100><font color=#8E4C28 size=2>$A_MES</font></TD>";

	}

	open(IN,"$TOWN_LIST") or &ERR("¥´¤£¶}«ü©wªº¤å¥ó¡C");
	@TOWN_DATA = <IN>;
	close(IN);
	($zwname,$wzc)=split(/<>/,$TOWN_DATA[0]);
	$zzhit=0;
	foreach(@TOWN_DATA){
		($zwname,$zwcon)=split(/<>/);
			if($wzc ne $zwcon){$zzhit=1;}
			$wzc = $zwcon;
	}


	&CHEACK_COM;
	if($mtime + $TIME_REMAKE < $date){
		if($mtime eq ""){
		$mtime = $date;
		&MAP_LOG("¹CÀ¸¶}©l¡C");
		}else{
		$mtime += $TIME_REMAKE;
		}
		$mmonth++;
		if($mmonth > 12){
			$myear++;
			$mmonth=1;
		}
		unshift(@month_new,"$myear<>$mmonth<>$mtime<>\n");
		if($ACT_LOG){
			($qsec,$qmin,$qhour,$qday) = localtime($mtime);
			unshift(@ACT_DATA,"===============\[$myear¦~$mmonth¤ë\]=================\n");
		}

		open(IN,"$COUNTRY_LIST") or &ERR2('¨S¶}¤å¥ó¡Cerr no :country');
		@COU_DATA = <IN>;
		close(IN);
		@NEW_COU_DATA=();
		foreach(@COU_DATA){
			($xvcid,$xvname,$xvele,$xvmark,$xvking,$xvmes,$xvsub,$xvpri)=split(/<>/);
			$xvmark++;
			push(@NEW_COU_DATA,"$xvcid<>$xvname<>$xvele<>$xvmark<>$xvking<>$xvmes<>$xvsub<>$xvpri<>\n");
		}
		open(OUT,">$COUNTRY_LIST") or &ERR('COUNTRY ¤£¯à¼g¤W¼Æ¾Ú¡C');
		print OUT @NEW_COU_DATA;
		close(OUT);

		$b_hit = 0;
		if($mmonth eq "1"){
			&MAP_LOG("$mmonth¤ë¡G<font color=orange>µ|ª÷</font>¤ä¥I¦UªZ±N¤u¸ê¡C");
			$b_hit = 1;
		}elsif($mmonth eq "7"){
			&MAP_LOG("$mmonth¤ë¡G<font color=orange>¦¬Ã¬</font>¤ä¥I¦UªZ±N¦ÌÂ³¡C");
			$b_hit = 1;
		}

		$eve_date = sprintf("%02d\¦~%02d\¤ë", $F_YEAR+$myear, $mmonth);
		$ihit=0;
		if(!int(rand(40))){
			$ihit=1;
			$ino = int(rand(6));
			if($ino eq 0){
				&MAP_LOG("<font color=red>¡i¨a®`¡j</font>\[$eve_date\]¤j¸s½ÀÂÎÅ§À»¥Ð¦a¡I");
				&MAP_LOG2("<font color=red>¡i¨a®`¡j</font>\[$eve_date\]¤j¸s½ÀÂÎÅ§À»¥Ð¦a¡I");
			}elsif($ino eq 1){
				&MAP_LOG("<font color=red>¡i¨a®`¡j</font>\[$eve_date\]¦b¦U¦aµo¥Í¤F¬x¤ô¡I");
				&MAP_LOG2("<font color=red>¡i¨a®`¡j</font>\[$eve_date\]¦b¦U¦aµo¥Í¤F¬x¤ô¡I");
			}elsif($ino eq 2){
				&MAP_LOG("<font color=red>¡i¨a®`¡j</font>\[$eve_date\]¬Ì¯f¬y¦æ¡C¤£¤Ö³£¥«ªº¤H¥Á¤]¨ü¨ì·P¬V¡C¡C");
				&MAP_LOG2("<font color=red>¡i¨a®`¡j</font>\[$eve_date\]¬Ì¯f¬y¦æ¡C¤£¤Ö³£¥«ªº¤H¥Á¤]·R¨ì·P¬V¡C¡C");
			}elsif($ino eq 3){
				&MAP_LOG("<font color=red>¡iÂ×§@¡j</font>\[$eve_date\]¹A§@ª«Â×¦¬¡A¦U¦a¹A¥ÁÁ|¦æ¼y¯¬¬¡°Ê¡C");
				&MAP_LOG2("<font color=red>¡iÂ×§@¡j</font>\[$eve_date\]¹A§@ª«Â×¦¬¡A¦U¦a¹A¥ÁÁ|¦æ¼y¯¬¬¡°Ê¡C");
			}elsif($ino eq 4){
				&MAP_LOG("<font color=red>¡i¨a®`¡j</font>\[$eve_date\]µo¥Í¤F¤j¦a¾_¡I");
				&MAP_LOG2("<font color=red>¡i¨a®`¡j</font>\[$eve_date\]µo¥Í¤F¤j¦a¾_¡I");
			}elsif($ino eq 5){
				&MAP_LOG("<font color=red>¡i°Ó©ô¡j</font>\[$eve_date\]¦U³£¥«ªº°Ó©±¿³©ô¼ö¾x¡C");
				&MAP_LOG2("<font color=red>¡i°Ó©ô¡j</font>\[$eve_date\]¦U³£¥«ªº°Ó©±¿³©ô¼ö¾x¡C");
			}
		}
		if($b_hit){

		# ¦æ±¡ÅÜ°Ê
		@NEW_TOWN_DATA=();
		foreach(@TOWN_DATA){
			($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7])=split(/<>/);
			if(!int(rand(2.0))){
				$zsouba += int(rand(0.5)*100)/100;
				if($zsouba > 1.2){
					$zsouba = 1.2;
				}
			}else{
				$zsouba -= int(rand(0.5)*100)/100;
				if($zsouba < 0.8){
					$zsouba = 0.8;
				}
			}
			if($zpri >= 50){
				$znum_add = int(80 * ($zpri - 50));
				if($znum_add < 500){$znum_add=500;}
				$znum += $znum_add;
				if($znum > $NOU_MAX){$znum=$NOU_MAX;}
			}else{
				$znum -= int(80 * (50 - $zpri));
				if($znum < 0){$znum=0;}
			}
			if($ihit){
				if($ino eq 0){
					$znou = int($znou * 0.8);
				}elsif($ino eq 1){
					$znou = int($znou * 0.9);
					$zsyo = int($zsyo * 0.9);
					$zshiro = int($zshiro * 0.9);
				}elsif($ino eq 2){
					$znum = int($znum * 0.8);
				}elsif($ino eq 3){
					$znou = int($znou * 1.2);
					if($znou > $znou_max){$znou=$znou_max;}
				}elsif($ino eq 4){
					$znou = int($znou * 0.8);
					$zsyo = int($zsyo * 0.8);
					$zshiro = int($zshiro * 0.8);
					$znum = int($znum * 0.9);
				}elsif($ino eq 5){
					$zsyo = int($zsyo * 1.1);
					if($zsyo > $zsyo_max){$zsyo=$zsyo_max;}
					$znum = int($znum * 1.1);
					if($znum > $NOU_MAX){$znum=$NOU_MAX;}
				}
			}

			push(@NEW_TOWN_DATA,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
		}
		open(OUT,">$TOWN_LIST");
		print OUT @NEW_TOWN_DATA;
		close(OUT);
		}
		open(OUT,">$month_read");
		print OUT @month_new;
		close(OUT);

	}
	if($ACT_LOG){
		if(@ACT_DATA > 800) { splice(@ACT_DATA,800); }
		open(OUT,">$actfile");
		print OUT @ACT_DATA;
		close(OUT);
	}

	$MESS1 = "<A href=\"$FILE_CONTNUE\">¡iÄ~Äò¹CÀ¸¡j</a>";
	$MESS2 = "<A href=\"$FILE_ENTRY\">¡i·s³Wµn¿ý¡j</a>";
	&roses_counter;
	$new_date = sprintf("%02d\¦~%02d\¤ë", $F_YEAR+$myear, $mmonth);
	$next_time = int(($mtime + $TIME_REMAKE - $date) / 60);


	&HEADER;
	print <<"EOM";
<!--[<a href=./i-index.cgi>Äâ±a¥Î</a>]-->
<CENTER>


<TABLE WIDTH="514" height=100% cellpadding="0" cellspacing="0" border=0><tr><td align=center>
<TABLE border=0 width=80% height=100% cellspacing=1>
    <TBODY>
          <TR>
          <TD align=center><p><TABLE height=140><TR><TD align=center><div align="center"><img src="image/title.gif" width="512" height="140"></div><p>
<font size=2 color=#ffffff><p><B>[$new_date]</b><BR>
¤U¦¸§ó·s<B>$next_time</B> ¤À<BR></font>
</TD></TR></TABLE>
<p align="center">
<table bgcolor=$TABLE_C align=center border=0>
<form action="$FILE_STATUS" method="POST"><input type="hidden" name="mode" value="STATUS"><TR><TH bgcolor=$TD_C2 height=5>¹CÀ¸±b¸¹</TH><td><input type="text" size="10" name="id" value="$_id"></td></TR>
<TR><TH bgcolor=$TD_C2 height=5>±b¸¹±K½X</tH><td><input type="password" size="10" name="pass" value="$_pass"></TD></TR>
<TR><td bgcolor=$TD_C1 align=center colspan=2><input type="submit" value="¶i¤J"></td></tr></table></form>
            $MESS2 
             
            <A href="$FILE_RANK">¡iµn¿ýªZ±N¤@Äý¡j</a> 
             
            <A href="./manual.html">¡i»¡©ú®Ñ¡j</A> 
			
            <a href="./map.cgi" target="blank">¡i¶Õ¤O¹Ï¡j</a> <p>

			<a href="$HOME_URL">¡i$HOME¡j</a>
			<a href="$BBS1_URL" target="blank">¡i$BBS1¡j</a>
			<a href="$LINK2_URL">¡i$LINK2¡j</a>
			<font color="#FFFFFF">³Ì¤jµn¿ý¤H¼Æ($ENTRY_MAX¤H)</font><br>

<TABLE width=80% BGCOLOR=$TABLE_C  cellspacing=1><TBODY>$mess</TBODY></TABLE>
<CENTER><HR width="514" size="0"><p align=right>[<font color=8E6C68>TOTAL ACCESS<font color=red><B> $total_count </font></B>HIT</font>]<BR>

</TD>
          </TR>
    <TR><TD>
    <table width="100%" border="0" align="center" cellspacing="0">
          <tr>
            <td><table width="100%" border="1" cellspacing="0" bordercolor="#996600">
                <tr>
                  <TD bgcolor=#EFE0C0 colspan="2" width=100% height="100"><font color=#8E4C28 size=2>$S_MES</font></TD>
                </tr>
                <tr>
                  <TD bgcolor=#EFE0C0 colspan="2" width=100% height="100"><font color=#8E4C28 size=2>$D_MES</font></TD>
                </tr>
               <tr>
                   $ACT_MES
              </tr></table></td>
          </tr>
        </table></TD></TR>       

        </TBODY>
      </TABLE>
</TR></TD></TABLE>

<form method=post action=./admin.cgi>
<font color="#FFFFFF">±b¸¹¡G</font><input type=text name=id size=7>
<font color="#FFFFFF">±K½X¡G</font><input type=pass name=pass size=7>
<input type=submit value="ºÞ²zªÌ">
</form>

EOM

	&FOOTER;
	exit;

}

sub roses_counter {

	$file_read = "./withlove_sgklog/counter.cgi";
	open(IN,"$file_read") or &ERR2('¥´¤£¶}¤å¥ó¡C');
	@reading = <IN>;
	close(IN);

	($total_count) = split(/<>/,$reading[0]);
	$total_count++;


	open(OUT,">$file_read");
	print OUT "$total_count\n";
	close(OUT);

}

sub CHEACK_COM{

	&D_F_LOCK;
	if (!-e $lockfile2) {&ERR2("¤å¥óÂê°ÝÃD¡C");}

	open(IN,"$TOWN_LIST");
	@TOWN_DATA = <IN>;
	close(IN);

	open(IN,"$UNIT_LIST") or &ERR("¥´¤£¶}«ü©wªº¤å¥ó¡C");
	@UNI_DATA = <IN>;
	close(IN);

	$zc=0;
	foreach(@TOWN_DATA){
		($z2name,$z2con,$z2num,$z2nou,$z2syo,$z2shiro)=split(/<>/);
		$town_name[$zc] = "$z2name";
		$town_cou[$zc] = "$z2con";
		$town_get[$z2con] += 1;
		$town_num[$z2con] += $z2num;
		$town_nou[$z2con] += $z2nou;
		$town_syo[$z2con] += $z2syo;
		$zc++;
	}


	$w_lock = 0;
	if($w_lock){
		open(LOCK,"> ./lock/sangoku") or &ERR2("Can't open lockfile: $!");
		flock(LOCK, 2)           or &ERR2("Can't flock        : $!");
	}

	$dir="./charalog/main";
	if($mmonth eq "1" || $mmonth eq "7"){
		opendir(dirlist,"$dir");
		while($file = readdir(dirlist)){
			if($file =~ /\.cgi/i){
				if(!open(page,"$dir/$file")){
					&ERR2("¥´¤£¶}¤å¥ó¡I");
				}
				@page = <page>;
				close(page);
				($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex) = split(/<>/,$page[0]);
				$cou_num[$kcon]++;
				$cex_total[$kcon]+=$kcex;
				push(@CL_DATA,"@page<br>");
			}
		}
		closedir(dirlist);
	}

	opendir(dirlist,"$dir");
	$kup_date=0;
	$thit=0;
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("¥´¤£¶}¤å¥ó¡I");
			}
			@page = <page>;
			close(page);
			($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/,$page[0]);
			if($kdate + $TIME_REMAKE < $date && $mtime > $kdate){
				$thit=1;
				($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex) = split(/,/,$ksub1);
				if($mmonth eq "1"){
					&SALARY;
					if($cou_num[$kcon] eq "0" || $cou_num[$kcon] eq ""){
						$cou_num[$kcon] = 1;
					}
					$kadd = 0;
					if($cex_total[$kcon] ne 0){
					$kadd  = int(($ksal * $kcex / $cex_total[$kcon]) + $kcex * 1.3);
					}
					$s_num = int($kclass / $LANK);
					if($s_num > 20){$s_num = 20;}
					if($kadd > 1000 + $s_num * 150){$kadd=1000 + $s_num * 150;}
					$kgold += $kadd;
					$k_ex_fol= ($kclass % $LANK)+$kcex;
					$kclass += $kcex;
					if($k_ex_fol > $LANK){
						$s_num = int($kclass / $LANK);
						if($s_num > 20){$s_num = 20;}
						$nadd = int(rand(3));
						if($nadd eq "1"){
							$kstr++;
							$add_m = "ªZ¤O";
						}elsif($nadd eq "2"){
							$kint++;
							$add_m = "ª¾¤O";
						}else{
							$klea++;
							$add_m = "²Î²v¤O";
						}
						$max_sal = 1000 + $s_num * 150;
						&K_LOG("$mmonth¤ë¡G¡i<font color=red>$add_m¤W¤É¤@ÂI¡I</font>¡j");						&K_LOG("$mmonth¤ë¡G¡i<font color=red>$LANK[$s_num]¤É®æ¡I</font>¡j¤u¸êªº³Ì¤j¤ä¥IÃBÅÜ¦¨<font color=red> $max_sal </font>¡I");

					}
					$kcex = 0;
					&K_LOG("$mmonth¤ë¡Gµ|ª÷¼x¦¬¤F<font color=red>$kadd</font>ª÷¡C");
				}elsif($mmonth eq "7"){
					&SALARY;
					if($cou_num[$kcon] eq "0" || $cou_num[$kcon] eq ""){
						$cou_num[$kcon] = 1;
					}
					$kadd = 0;
					if($cex_total[$kcon] ne 0){
						$kadd  = int(($ksal * $kcex / $cex_total[$kcon]) + $kcex * 1.3);
					}
					$s_num = int($kclass / $LANK);
					if($s_num > 20){$s_num = 20;}
					if($kadd > 1000 + $s_num * 150){$kadd=1000 + $s_num * 150;}
					$krice += $kadd;
					$k_ex_fol= ($kclass % $LANK)+$kcex;
					$kclass += $kcex;
					if($k_ex_fol > $LANK){
						$s_num = int($kclass / $LANK);
						if($s_num > 20){$s_num = 20;}
						$nadd = int(rand(3));
						if($nadd eq "1"){
							$kstr++;
							$add_m = "ªZ¤O";
						}elsif($nadd eq "2"){
							$kint++;
							$add_m = "ª¾¤O";
						}else{
							$klea++;
							$add_m = "²Î²v¤O";
						}
						$max_sal = 1000 + $s_num * 150;
						&K_LOG("$mmonth¤ë¡G¡i<font color=red>$add_m¤W¤É¤@ÂI¡I</font>¡j");						&K_LOG("$mmonth¤ë¡G¡i<font color=red>$LAMK[$s_num]¤É®æ¡I</font>¡j¤u¸êªº³Ì¤j¤ä¥IÃBÅÜ¦¨<font color=red> $max_sal </font>¡I");
					}
					$kcex = 0;
					&K_LOG("$mmonth¤ë¡G­¹®Æ¦¬Ã¬±o¨ì<font color=red>$kadd</font>¡C");
				}
				open(IN,"./charalog/command/$kid\.cgi");
				@COM_DATA = <IN>;
				close(IN);
				($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/,$COM_DATA[0]);

				$kdate += $TIME_REMAKE;
				&CHARA_MAIN_INPUT;
				splice(@COM_DATA,0,1);
				push(@COM_DATA,"<><><><><><><>\n");

				open(OUT,">./charalog/command/$kid\.cgi");
				print OUT @COM_DATA;
				close(OUT);

				($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7])=split(/<>/,$TOWN_DATA[$kpos]);
				if($zcon eq "$kcon" || $cid eq "20" || $cid eq "21" || $cid eq "27" || $cid eq "0" || $cid eq ""){

					$kprodmg = 0;
					if($kbook ne "" && $kbook ne 0){
						open(IN,"$PRO_LIST");
						@PRO_DATA = <IN>;
						close(IN);
						($kproname,$kproval,$kprodmg) = split(/<>/,$PRO_DATA[$kbook]);
					}
					if($cid eq "1"){
						$ksub2=0;
						if($kgold<50){
							&K_LOG("$mmonth¤ë¡G¸êª÷¤£¨¬¤£¯à¹ê¦æ¡C");
						}else{
							$znouadd = int(($kint+$kprodmg)/12 + rand(($kint+$kprodmg)) / 20);
							$znou += $znouadd;
							$kgold -= 50;
							if($znou > $znou_max){
								$znou = $znou_max;
							}
							$kcex += 30;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
							}
							&K_LOG("$mmonth¤ë¡G$znameªº¹A·~¶}µo<font color=red>+$znouadd</font>¡C");
							$kint_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}elsif($cid eq "2"){
						$ksub2=0;
						if($kgold<50){
							&K_LOG("$mmonth¤ë¡G¸êª÷¤£¨¬¤£¯à¹ê¦æ¡C");
						}else{
							$zsyoadd = int(($kint+$kprodmg)/12 + rand(($kint+$kprodmg)) / 20);
							$zsyo += $zsyoadd;
							$kgold -= 50;
							if($zsyo > $zsyo_max){
								$zsyo = $zsyo_max;
							}
							$kcex += 30;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
							}
							&K_LOG("$mmonth¤ë¡G$znameªº°Ó·~µo®i<font color=red>+$zsyoadd</font>¡C");
							$kint_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}elsif($cid eq "3"){
						$ksub2=0;
						if($kgold<50){
							&K_LOG("$mmonth¤ë¡G¸êª÷¤£¨¬¤£¯à¹ê¦æ¡C");
						}else{
							$zshiroadd = int(($kint+$kprodmg)/12 + rand(($kint+$kprodmg)) / 20);
							$zshiro += $zshiroadd;
							$kgold -= 50;
							if($zshiro > $zshiro_max){
								$zshiro = $zshiro_max;
							}
							$kcex += 30;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
							}
							&K_LOG("$mmonth¤ë¡G$znameªº«°Àð±j¤Æ<font color=red>+$zshiroadd</font>¡C");
							$kint_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}elsif($cid eq "8"){
						$ksub2=0;
						if($krice<50){
							&K_LOG("$mmonth¤ë¡G¦Ì¤£¨¬¤£¯à¹ê¦æ¡C");
						}else{
							$zpriadd = int($kcha/20 + rand($kcha) / 20);
							$zpri += $zpriadd;
							$krice -= 50;
							if($zpri > 100){
								$zpri = 100;
							}
							$kcex += 30;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
							}
							&K_LOG("$mmonth¤ë¡G$znameªº¥Á©¾<font color=red>+$zpriadd</font>¡C");
							$kcha_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}elsif($cid eq "10"){
						$ksub2=0;
						if($ksol eq "$klea" && $csub eq $ksub1_ex){
							&K_LOG("$mmonth¤ë¡G¡i­x¨Æ¡j¡G¤h§L¼Æ¤w¹F¤W­­¡C");
						}elsif($kgold < $cnum * $SOL_PRICE[$csub]){
							&K_LOG("$mmonth¤ë¡G¡i­x¨Æ¡j¡G©Ò«ùª÷¤£¨¬¡C");
						}elsif($znum < $cnum * 10){
							&K_LOG("$mmonth¤ë¡G¡i­x¨Æ¡j¡G¹A¥Á¤£¨¬°÷¡C");
						}elsif($zpri < int($cnum / 10)){
							&K_LOG("$mmonth¤ë¡G¡i­x¨Æ¡j¡G¹A¥Á©Úµ´¡C");
						}else{
							if($ksub1_ex eq $csub || $ksub1_ex eq "" && $csub eq 0){
								if($ksol + $cnum > $klea){
									$cnum = $klea - $ksol;
								}
								$ksol += $cnum;
							}else{
								if($cnum > $klea){
									$cnum = $ksol;
								}
								$ksol = $cnum;
							}
							$kgat -= $cnum;
							if($kgat < 0 ){
								$kgat = 0;
							}
							$ksub1_ex = $csub;
							$kcex += 10;
							$kgold -= $cnum * $SOL_PRICE[$csub];
							$znum -= $cnum * 5;
							$zpri -= int($cnum / 10);
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
							}
							&K_LOG("$mmonth¤ë¡G$SOL_TYPE[$ksub1_ex]¼x§L<font color=red>$cnum</font>¤H¡C");
							$kstr_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}elsif($cid eq "11"){
						$ksub2=0;
						$kgat += int($klea/6 + rand($klea/6));
						if($kgat > 100){
							$kgat = 100;
						}
						$kcex += 15;
						&K_LOG("$mmonth¤ë¡G¤h§Lªº°V½m«×ÅÜ¦¨<font color=red>$kgat</font>¡C");
						$klea_ex++;
						$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
					}elsif($cid eq "12"){
						$ksub2=0;
						if($ksol eq "0" || $ksol eq ""){
							&K_LOG("$mmonth¤ë¡G¨S¦³¤h§L¤£¯à¦u³Æ¡C");
						}else{
							open(IN,"$DEF_LIST");
							@DEF_LIST = <IN>;
							close(IN);
							my @NEW_DEF_LIST2=();
							$whit=0;
							foreach(@DEF_LIST){
								($tid,$tname,$ttown_id,$ttown_flg,$tcon) = split(/<>/);
								if("$tid" eq "$kid"){
								}else{
									push(@NEW_DEF_LIST2,"$_");
								}
							}
							unshift(@NEW_DEF_LIST2,"$kid<>$kname<>$kpos<>0<>$kcon<>\n");
							open(OUT,">$DEF_LIST");
							print OUT @NEW_DEF_LIST2;
							close(OUT);
							$kcex += 25;
							&K_LOG("$mmonth¤ë¡G$zname¦u³Æ¡C");
							$kcha_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}elsif($cid eq "18"){
						$ksub2=0;
						($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7])=split(/<>/,$TOWN_DATA[$cnum]);
						if($zcon eq $kcon){
							&K_LOG("$mmonth¤ë¡G¤£¯à§ðÀ»¦Û°ê¡C");
						}elsif($z[0] ne $kpos && $z[1] ne $kpos && $z[2] ne $kpos && $z[3] ne $kpos && $z[4] ne $kpos && $z[5] ne $kpos && $z[6] ne $kpos && $z[7] ne $kpos ){
							&K_LOG("$mmonth¤ë¡G$zname¨S¦³¾F±µ¡C");
						}else{
							open(IN,"$COUNTRY_LIST");
							@COU_DATA = <IN>;
							close(IN);
							@NEW_COU_DATA=();
							$zvhit=0;
							foreach(@COU_DATA){
								($xvcid,$xvname,$xvele,$xvmark,$xvking,$xvmes,$xvsub,$xvpri)=split(/<>/);
								if($xvcid eq $zcon){$zvhit=1;last;}
							}
							if($zvhit && $xvmark < 36){
								&K_LOG("$mmonth¤ë¡G$xvname§ðÀ»¡C($xvmark¦^¦X)");
							}else{
								&COUNTRY_DATA_OPEN("$kcon");
								if($xmark < 36){
									&K_LOG("$mmonth¤ë¡G$xname§ðÀ»¡C($xmark¦^¦X)");
								}else{
									open(IN,"$DEF_LIST");
									@DEF_LIST3 = <IN>;
									close(IN);
									$d_hit=0;
									foreach(@DEF_LIST3){
										($mdid,$mdname,$mdtown_id,$mdtown_flg,$mdcon) = split(/<>/);
										if($cnum eq $mdtown_id){
											$d_hit=1;last;
										}
									}
									$katt_add2 = 0;
									if("$xdai" eq "$kid"){
										$katt_add2 = 10;
									}elsif("$xuma" eq "$kid"){
										if($ksub1_ex eq "3"){
											$katt_add2 = 10;
										}
									}elsif("$xgoei" eq "$kid"){
										if($ksub1_ex eq "2"){
											$katt_add2 = 10;
										}
									}elsif("$xyumi" eq "$kid"){
										if($ksub1_ex eq "1"){
											$katt_add2 = 10;
										}
									}elsif("$xhei" eq "$kid"){
										if($ksub1_ex eq "0"){
											$katt_add2 = 10;
										}
									}

									$kcex += 20;
									&MAP_LOG("$xnameªº$kname§ð¶i¤F$zname¡C");
									$eid="";
									if($d_hit){
										open(IN,"./charalog/main/$mdid\.cgi");
										@E_DATA = <IN>;
										close(IN);
										($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);
				($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex) = split(/,/,$esub1);
										$last_battle=0;
									}else{
										$ename = "«°Àð";
										$esol = $zshiro;
										$estr = int($zdef_att/15)+30;
										$egat = 60;
										$last_battle=1;
										$esub1_ex="";
									}

									&K_LOG2("$mmonth¤ë¡G$xnameªº$kname§ð¶i¤F$zname¡C");
									&E_LOG2("$mmonth¤ë¡G$xnameªº$kname»P$enameµo¥Í¾Ô°«¡I");

									&CHARA_ITEM_OPEN;

									if($ksub1_ex eq "1"){
										$katt_add = 10;
										$katt_def = 0;
									}elsif($ksub1_ex eq "2"){
										$katt_add = 0;
										$katt_def = 15;
									}elsif($ksub1_ex eq "3"){
										$katt_add = 20;
										$katt_def = 10;
									}elsif($ksub1_ex eq "4"){
										$katt_add = 40;
										$katt_def = 0;
									}elsif($ksub1_ex eq "5"){
										$katt_add = $kint;
										$katt_def = 0;
									}else{
										$katt_add = 0;
										$katt_def = 0;
									}
									if($esub1_ex eq "1"){
										$eatt_add = 10;
										$eatt_def = 0;
									}elsif($esub1_ex eq "2"){
										$eatt_add = 0;
										$eatt_def = 15;
									}elsif($esub1_ex eq "3"){
										$eatt_add = 20;
										$eatt_def = 10;
									}elsif($esub1_ex eq "4"){
										$eatt_add = 40;
										$eatt_def = 0;
									}elsif($esub1_ex eq "5"){
										$eatt_add = $eint;
										$eatt_def = 0;
									}else{
										$eatt_add = 0;
										$eatt_def = 0;
									}

									$katt = int(($kstr + $karmdmg + $katt_add + $katt_add2 - $eatt_def - int($egat / 2.5))/8);
									if($katt < 0){$katt = 0;}
									$eatt = int(($estr + $earmdmg + $eatt_add - $katt_def - int($kgat / 2.5))/8);
									$kex_add=0;
									$eex_add=0;
									if($eatt < 0){$eatt = 0;}
									$win=0;
									for($count=0;$count<50;$count++){
										$kdmg=0;
										$edmg=0;
										if($ksol <= 0){last;}
										$kdmg = int(rand($katt));
										if($kdmg <= 0){$kdmg=1;}
										$wsol = $esol;
										$esol -= $kdmg;
										
										$kex_add += ($wsol - $esol);
										if($esol <= 0){
											$esol=0;
											&K_LOG2("¦^¦X<font color=red>$count</font>¡G$kname $SOL_TYPE[$ksub1_ex] $ksol¤H ¡õ\(-$edmg\) |$ename $SOL_TYPE[$esub1_ex] $esol¤H ¡õ\(-$kdmg\)");
											&E_LOG2("¦^¦X<font color=red>$count</font>¡G$kname $SOL_TYPE[$ksub1_ex] $ksol¤H ¡õ\(-$edmg\) |$ename $SOL_TYPE[$esub1_ex] $esol¤H ¡õ\(-$kdmg\)");
											$win = 1;last;
										}

										$edmg = int(rand($eatt));
										if($edmg <= 0){$edmg=1;}
										$wsol = $ksol;
										$ksol -= $edmg;
										$eex_add += ($wsol - $ksol);
										if($ksol <= 0){
											$ksol=0;
											&K_LOG2("¦^¦X<font color=red>$count</font>¡G$kname $SOL_TYPE[$ksub1_ex] $ksol¤H ¡õ\(-$edmg\) |$ename $SOL_TYPE[$esub1_ex] $esol¤H ¡õ\(-$kdmg\)");
											&E_LOG2("¦^¦X<font color=red>$count</font>¡G$kname $SOL_TYPE[$ksub1_ex] $ksol¤H ¡õ\(-$edmg\) |$ename $SOL_TYPE[$esub1_ex] $esol¤H ¡õ\(-$kdmg\)");
											last;
										}
										&K_LOG2("¦^¦X<font color=red>$count</font>¡G$kname $SOL_TYPE[$ksub1_ex] $ksol¤H ¡õ\(-$edmg\) |$ename $SOL_TYPE[$esub1_ex] $esol¤H ¡õ\(-$kdmg\)");
									}

									$eex_add = int($eex_add/2);
									$kex_add = int($kex_add/2);
									if($win){
										$ksub2_ex++;
										if($last_battle){
											if($town_get[$zcon] <= 1){
												@NEW_COU=();
												foreach(@COU_DATA){
													($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
													if("$zcon" eq "$xcid"){
													}else{
														push(@NEW_COU,"$_");
													}
												}
												open(OUT,">$COUNTRY_LIST");
												print OUT @NEW_COU;
												close(OUT);
												&MAP_LOG2("<font color=red>¡i·À¤`¡j</font>\[$old_date\]$cou_name[$zcon]·À¤`¡C¡C");
												&MAP_LOG("<font color=red>¡i·À¤`¡j</font>\[$old_date\]$cou_name[$zcon]·À¤`¡C¡C");
											}
												$zcon = $kcon;
												$znou = int($znou*0.8);
												$zsyo = int($zsyo*0.8);
												$znum = int($znum*0.8);
												$zsub1 = int($zsub1*0.8);
												$zdef_att = 0;
												$zpri = int($zpri*0.8);
												$kex_add += 50;
												$kcex += $kex_add;
												$kpos = $cnum;
											@NEW_DEF_LIST3=();
											$pphit=0;
											foreach(@DEF_LIST3){
												($did,$dname,$dtown_id,$dtown_flg,$dcon) = split(/<>/);
												if("$did" eq "$kid"){
													$pphit=1;
													unshift(@NEW_DEF_LIST3,"$kid<>$kname<>$kpos<>0<>$kcon<>\n");
												}else{
													push(@NEW_DEF_LIST3,"$_");
												}
											}

											if(!$pphit){
												unshift(@NEW_DEF_LIST3,"$kid<>$kname<>$kpos<>0<>$kcon<>\n");
											}
											open(OUT,">$DEF_LIST");
											print OUT @NEW_DEF_LIST3;
											close(OUT);

											&K_LOG2("<font color=blue>$zname</font>¤J¤â¡I±o¨ì¤F<font color=red>$kex_add</font>°^Äm­È¡I");
											&MAP_LOG2("<font color=blue>¡i¤ä°t¡j</font>\[$old_date\]$cou_name[$kcon]ªº$kname¤ä°t¤F$zname¡C");
											&MAP_LOG("<font color=blue>¡i¤ä°t¡j</font>\[$old_date\]$cou_name[$kcon]ªº$kname¤ä°t¤F$zname¡C");
										}else{
											@NEW_DEF_LIST3=();
											foreach(@DEF_LIST3){
												($did,$dname,$dtown_id,$dtown_flg,$dcon) = split(/<>/);
												if("$mdid" ne "$did"){
													push(@NEW_DEF_LIST3,"$_");
												}
											}
											open(OUT,">$DEF_LIST");
											print OUT @NEW_DEF_LIST3;
											close(OUT);
											$kex_add += 30;
											$kcex += $kex_add;
											$ecex += $eex_add;
											&K_LOG2("$knameÀ»­Ë¤F$ename¡I±o¨ì¤F<font color=blue>$kex_add</font>°^Äm­È¡I");
											&E_LOG2("$ename $kname±Ñ¥_¡C¡C±o¨ì¤F<font color=red>$eex_add</font>°^Äm­È¡I");
											&MAP_LOG("<font color=blue>¡i³Ó§Q¡j</font>$knameÀ»­Ë¤F$ename¡C");
										}
									}else{
										$eex_add += 30;
										$ecex += $eex_add;
										$kcex += $kex_add;
										&K_LOG2("$kname $ename±Ñ¥_¡C¡C±o¨ì¤F<font color=red>$kex_add</font>°^Äm­È¡I");
										&E_LOG2("$enameÀ»­Ë$kname¡I±o¨ì¤F<font color=blue>$eex_add</font>°^Äm­È¡I");
									}

									if(!$last_battle){
										if($eid ne ""){
											&ENEMY_INPUT;
										}
									}else{
										$zshiro = $esol;
										$zdef_att -= $kex_add;
										if($zdef_att < 0){
											$zdef_att=0;
										}
										if("$zname" ne ""){
											splice(@TOWN_DATA,$cnum,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");

										}
									}

									$kstr_ex++;
									$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
								}
							}
						}
					}elsif($cid eq "19"){
						$ksub2=0;
						if($csub){
							if($cnum > 3000){
								$cnum = 3000;
							}
							if($cno){
								if($kgold > int($cnum / $csub)){
									$kadd = int($cnum / $csub);
									$kgold -= $kadd;
									$krice += $cnum;
									&K_LOG("$mmonth¤ë¡G¡i°Ó¤H¡j:¤ä¥I$kaddª÷¡AÁÊ¶R¤F$cnum¦Ì¡C");
								$kint_ex++;
								$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
								}else{
									&K_LOG("$mmonth¤ë¡G¡i°Ó¤H¡j¡G©Ò«ùª÷¤£¨¬¡C");
								}
							}else{
								if($krice > $cnum * $csub){
									$kadd = int($cnum * $csub);
									$krice -= $kadd;
									$kgold += $cnum;
									&K_LOG("$mmonth¤ë¡G¡i°Ó¤H¡j¡G½æ¥X$kadd¦Ì¡A$cnumª÷¼W¥[¡C");
								$kint_ex++;
								$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
								}else{
									&K_LOG("$mmonth¤ë¡G¡i°Ó¤H¡j¡G¦Ì¤£¨¬¡C");
								}
							}
						}
					}elsif($cid eq "20"){
						$ksub2=0;
						$zhit=0;
						foreach(@z){
							if($_ eq $cnum){
								$zhit=1;
							}
						}
						if($zhit){
							$kpos = $cnum;
							$klea_ex++;
							if($xcid ne "0"){
								$kcex += 20;
							}
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
							&K_LOG("$mmonth¤ë¡G$town_name[$cnum]²¾°Ê¡C");
						}else{
							&K_LOG("$mmonth¤ë¡G$town_name[$cnum]¤£¯à²¾°Ê¡C²{¦b¦ì¸m¡G$zname");
						}
					}elsif($cid eq "21"){
						$ksub2=0;
						&COUNTRY_DATA_OPEN($kcon);
						if($xcid eq 0){
							if($cou_name[$cnum] eq ""){
								&K_LOG("$mmonth¤ë¡G¨º­Ó°ê®a¤£¯à¥K©x¡C");
							}else{
								if(@B_LIST eq "0"){
									open(IN,"./withlove_sgklog/black_list.cgi");
									@B_LIST = <IN>;
									close(IN);
								}
								$b_hit=0;
								foreach(@B_LIST){
									($bid,$bcon,$bname,$bsub) = split(/<>/);
									if($bid eq $kid && $bcon eq $kcon){
										$b_hit=1;
									}
								}
								if($b_hit){
									&K_LOG("$mmonth¤ë¡G$cou_name[$cnum]¥K©x³Q©Úµ´¤F¡C");
								}else{
									$kcon = $cnum;
									&K_LOG("$mmonth¤ë¡G$cou_name[$cnum]¥K©x¡C");
									&MAP_LOG("$mmonth¤ë¡G$kname $cou_name[$cnum]¥K©x¡C");
								}
							}
						}else{
							&K_LOG("$mmonth¤ë¡G¤£¯à¥K©x¡C");
						}
					}elsif($cid eq "22"){
						$ksub2=0;
						open(IN,"$ARM_LIST");
						@ARM_DATA = <IN>;
						close(IN);
						($armname,$armval,$armdmg,$armwei,$armele,$armsta,$armclass,$armtownid) = split(/<>/,$ARM_DATA[$cnum]);
						($armname2,$armval2) = split(/<>/,$ARM_DATA[$karm]);
						$armval2 = int($armval2 * 0.6);
						if($armval > $kgold + $armval2){
							&K_LOG("$mmonth¤ë¡G©Ò«ùª÷¤£¨¬¡C$armname ª÷¡G$armval");
						}else{
							$kgold += $armval2;
							$kgold -= $armval;
							$karm = $cnum;
							&K_LOG("$mmonth¤ë¡GªZ¾¹¡G$armname2<font color=red>$armval2</font>ª÷½æ¥X¡A$armnameÁÊ¤J¡C");
						}
					}elsif($cid eq "23"){
						$ksub2=0;
						open(IN,"$PRO_LIST");
						@PRO_DATA = <IN>;
						close(IN);
						($proname,$proval,$prodmg,$prowei,$proele,$prosta,$proclass,$protownid) = split(/<>/,$PRO_DATA[$cnum]);
						($proname2,$proval2) = split(/<>/,$PRO_DATA[$kbook]);
						$proval2 = int($proval2 * 0.6);
						if($proval > $kgold + $proval2){
							&K_LOG("$mmonth¤ë¡G©Ò«ùª÷¤£¨¬¡C$proname ª÷¡G$proval");
						}else{
							$kgold += $proval2;
							$kgold -= $proval;
							$kbook = $cnum;
							&K_LOG("$mmonth¤ë¡G®ÑÄy¡G$pronameÁÊ¤J¡C");
						}
					}elsif($cid eq "25"){
						$ksub2=0;
						if($kgold < 100){
							&K_LOG("$mmonth¤ë¡G©Ò«ùª÷¤£¨¬¡C");
						}else{

							$kgold-=100;
							$kcex += 30;
							open(IN,"$MESSAGE_LIST2");
							@MES_REG2 = <IN>;
							close(IN);
							$mes_num = @MES_REG2;
							if($mes_num > $MES_MAX) { pop(@MES_REG2); }
							unshift(@MES_REG2,"$cnum<>$kid<>$kpos<>$kname<>$csub<>$cno<>$ctime<>$kchara<>$cend<>\n");
							open(OUT,">$MESSAGE_LIST2");
							print OUT @MES_REG2;
							close(OUT);
							&K_LOG("$mmonth¤ë¡G$cno±K®Ñµo°e¡C");
							$kcha_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}elsif($cid eq "27"){
						$ksub2=0;
						if($kgold < 50){
							&K_LOG("$mmonth¤ë¡G©Ò«ùª÷¤£¨¬¡C");
						}else{
							if($cnum eq "1"){
								$kstr_ex +=2;
								$a_mes = "ªZ¤O";
							}elsif($cnum eq "2"){
								$kint_ex +=2;
								$a_mes = "ª¾¤O";
							}else{
								$klea_ex +=2;
								$a_mes = "²Î²v¤O";
							}
							$kgold-=50;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
							&K_LOG("$mmonth¤ë¡G$a_mes±j¤Æ¡C");
						}
					}elsif($cid eq "28"){
						$ksub2=0;
						$uhit=0;
						foreach(@UNI_DATA){
							($unit_id,$uunit_name,$ucon,$ureader,$uid)=split(/<>/);
							if("$uid" eq "$kid" && $unit_id eq $kid){$uhit=1;last;}
						}
						if(!$uhit){
							&K_LOG("$mmonth¤ë¡G¶¤ªø¥H¥~¤£¯à¹ê¦æ¡C");
						}else{

							foreach(@UNI_DATA){
								($unit_id,$uunit_name,$ucon,$ureader,$uid)=split(/<>/);
								if($unit_id eq $kid && $uid ne $unit_id){
									open(IN,"./charalog/main/$uid.cgi");
									@E_DATA = <IN>;
									close(IN);
									($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);								
									$epos = $kpos;
									if($eid ne ""){
										&E_LOG2("$mmonth¤ë¡G$uunit_name³¡¶¤¶¤ªø©R¥O$town_name[$kpos]¶°¦X¡C");
										&ENEMY_INPUT;
									}
								}
							}
							$klea_ex++;
							$kcex+=10;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
							&K_LOG("$mmonth¤ë¡G$uunit_name³¡¶¤$town_name[$kpos]¶°¦X¡C");
						}
					}elsif($cid eq "29"){
						$ksub2=0;
						if($kgold<50){
							&K_LOG("$mmonth¤ë¡G¸êª÷¤£¨¬¤£¯à¹ê¦æ¡C");
						}else{
							$ztecadd = int(($kint+$kprodmg)/12 + rand(($kint+$kprodmg)) / 20);
							$zsub1 += $ztecadd;
							$kgold -= 50;
							if($zsub1 > 999){
								$zsub1 = 999;
							}
							$kcex += 30;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
							}
							&K_LOG("$mmonth¤ë¡G$zname§Þ³N¶}µo¡G<font color=red>+$ztecadd</font>¡C");
							$kint_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}elsif($cid eq "30"){
						$ksub2=0;
						if($kgold<50){
							&K_LOG("$mmonth¤ë¡G¸êª÷¤£¨¬¤£¯à¹ê¦æ¡C");
						}else{
							$zdef_att_add = int(($kint+$kprodmg)/12 + rand(($kint+$kprodmg)) / 20);
							$zdef_att += $zdef_att_add;
							$kgold -= 50;
							if($zdef_att > 999){
								$zdef_att = 999;
							}
							$kcex += 30;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
							}
							&K_LOG("$mmonth¤ë¡G$zname«°Àð­@¤[¤O±j¤Æ¡G<font color=red>+$zdef_att_add</font>¡C");
							$kint_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}else{
						$ksub2++;
						if($ksub2 > $DEL_TURN){
							unlink("./charalog/main/$kid\.cgi");
							unlink("./charalog/log/$kid\.cgi");
							unlink("./charalog/command/$kid\.cgi");
							&MAP_LOG("[¶¢¸m]¡G$kname±b¸¹§R°£¡C");
							next;
						}
						&K_LOG("$mmonth¤ë¡G¨S¦³¶µ¥Ø¹ê¦æ¡C");
					}

				}else{
					&K_LOG("$mmonth¤ë¡G¤£¬O¥»°ê¡C");
				}

				$krice -= $ksol;
				if($krice < 0){
					&K_LOG("$mmonth¤ë¡G<font color=red>¡i°k²æ¡j</font>¡G¤£¯à¤ä¥I¦Ì¤©¤h§L¡A¤h§L°k²æ¡I");
					$ksol = 0;
					$krice = 0;
				}

				$uhit=0;
				if($kstr_ex >= 10){
					$kstr++;
					$kstr_ex-=10;
					$uhit=1;
					&K_LOG("$mmonth¤ë¡G<font color=red>¡i¤W¤É¡j</font>:$knameªºªZ¤O¢°ÂI¤W¤É¡C");
				}
				if($kint_ex >= 10){
					$kint++;
					$kint_ex-=10;
					$uhit=1;
					&K_LOG("$mmonth¤ë¡G<font color=red>¡i¤W¤É¡j</font>:$knameªºª¾¤O¢°ÂI¤W¤É¡C");
				}
				if($klea_ex >= 10){
					$klea++;
					$klea_ex-=10;
					$uhit=1;
					&K_LOG("$mmonth¤ë¡G<font color=red>¡i¤W¤É¡j</font>:$knameªº²Î²v¤O¢°ÂI¤W¤É¡C");
				}
				if($kcha_ex >= 10){
					$kcha++;
					$kcha_ex-=10;
					$uhit=1;
					&K_LOG("$mmonth¤ë¡G<font color=red>¡i¤W¤É¡j</font>:$knameªº¤H±æ¤@ÂI¤W¤É¡C");
				}
				if($uhit){
					$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
				}

				&CHARA_MAIN_INPUT;

				if($ACT_LOG){
					($qsec,$qmin,$qhour,$qday) = localtime($kdate);
					unshift(@ACT_DATA,"$kname§ó·s\($qday¤é $qhour:$qmin:$qsec\)\n");
				}
				$kup_date++;
				if($kup_date > 10){last;}
			}
		}
	}
	if($thit){
		foreach(@TOWN_DATA){
			$data .= $_;
		}
		&lock("xxx","1") or &ERR2("¤å¥óÂê¥¢±Ñ¡C");
		&data_save("./withlove_sgklog","town_data.cgi","$data");
		&unlock("xxx");
	}

	closedir(dirlist);
	&D_UNLOCK_FILE;
}


#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/      ¡@ LOGªº¼g¤J‚Ý      _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub E_LOG2 {

	if($eid ne ""){
		open(IN,"./charalog/log/$eid\.cgi");
		@E_LOG2 = <IN>;
		close(IN);
		unshift(@E_LOG2,"$_[0]($mday¤é$hour®É$min¤À)\n");
		splice(@E_LOG2,20);

		open(OUT,">./charalog/log/$eid\.cgi");
		print OUT @E_LOG2;
		close(OUT);
	}
}

sub K_LOG2 {

	open(IN,"./charalog/log/$kid\.cgi");
	@K_LOG2 = <IN>;
	close(IN);
	unshift(@K_LOG2,"$_[0]($mday¤é$hour®É$min¤À)\n");
	splice(@K_LOG2,20);
	open(OUT,">./charalog/log/$kid\.cgi");
	print OUT @K_LOG2;
	close(OUT);
}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/¡@¡@¡@¡@ ¤u¸ê­pºâ¡@ ¡@¡@¡@_/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub SALARY {

	$ksal=0;
	foreach(@TOWN_DATA){
		($z2name,$z2con,$z2num,$z2nou,$z2syo,$z2shiro)=split(/<>/);
		if($z2con eq $kcon){
			if($mmonth eq "1"){
				$ksal += int($z2syo * 8 * $z2num / 10000);
			}elsif($mmonth eq "7"){
				$ksal += int($z2nou * 8 * $z2num / 10000);
			}
		}
	}

}

#_/_/_/_/_/_/_/_/_/_/_/_/#
#       FILE LOCK        #
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub D_F_LOCK {

	local($retry)=1;
	if (-e $lockfile2) {
		local($mtime) = (stat($lockfile2))[9];
		if ($mtime && $mtime < time - 60) { &D_UNLOCK_FILE; }
	}

	while (!mkdir($lockfile2, 0755)) {
		if (--$retry <= 0) { &ERR2("File lock error!<BR>¼Æ¾Ú§ó·s¤¤¡C½Ðµy«á¦A¸Õ¡C");
}
		sleep(1);
	}
}

#_/_/_/_/_/_/_/_/_/_/_/_/#
#     FILE UNLOCK        #
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub D_UNLOCK_FILE
{
  rmdir("$lockfile2");
}

sub data_save {
        local($datapath) = $_[0];
		local($file) = $_[1];
		local($data) = "$_[2]";
		local($datafile) = $datapath . '/' . $file;
		local($tmpfile) = $datapath . '/' . $file . '.tmp';
		local($tmp_dummy) = $datapath . '/' . $file . "$$\.tmp";
		local($datadir) = $datapath . '/';
		opendir(DIR, $datadir) ;
		@list = readdir(DIR) ;
		closedir(DIR) ;
		foreach (@list) {
			if ($_ =~ /($file).*\.tmp$/) {
				&ERR2("Temporary File ¦s¦b¡C<br>");
			}
		}
		if(!open(TMP,">$tmpfile")){
			&ERR2("Temporary File ¤£¯à§@¦¨¡C<br>");
		}elsif(!close(TMP)){
			&ERR2("Temporary Tile ¤£¯à§@¦¨¡C<br>");
		}elsif(!open(DMY,">$tmp_dummy")){
			&ERR2("¦¬ÂÃ¥Îªº¼È¦s¤å¥ó¤£¯à§@¦¨¡C<br>");
		}elsif(!close(DMY)){
			&ERR2("¤£¯à¨Ï¥Î¼È¦s¤å¥ó¡C<br>");
		}elsif(!chmod (0666,"$tmp_dummy")){
			&ERR2("¦¬ÂÃ¥Îªº¼È¦s¤å¥óÄÝ©Ê¤£¯àÅÜ§ó¡C<br>");
		}elsif(!open(DMY,">$tmp_dummy")){
			&ERR2("¦¬ÂÃ¥Îªº¼È¦s¤å¥ó¤£¯à¶}©ñ¡C<br>");
		}
		print DMY $data;
		if (!close(DMY)){
			&ERR2("¦¬ÂÃ¥Îªº¼È¦s¤å¥ó¤£¯à«O¦s¡C<br>");
		}elsif(!rename("$tmp_dummy" , "$datafile")){
			&ERR2("¦¬ÂÃ¥Îªº¼È¦s¤å¥ó§ó¦W¤£¯à§¹¦¨¡C<br>");
		}elsif(!unlink ("$tmpfile")){
			&ERR2("Temporary File ¤£¯à§R±¼¡C<br>");
		}
}

sub lock #($file_name, $use_lock)
{
	local($file_name, $use_lock) = @_;
	local($lock_flag) = $file_name . ".lock";

	if ($use_lock) {
	local($i) = 0;
#	return -1 if (!-f $file_name);
	rmdir($lock_flag) if (-d $lock_flag && time - (stat($lock_flag))[9] > 60);
	while(!mkdir($lock_flag, 0755)) {
	select(undef, undef, undef, 0.05);
		return 0 if (++ $i >= 100);
		}
		return 1;
 	}
 	return 1;
}

sub unlock
{
  rmdir("$_[0].lock") if (-d "$_[0].lock");
}

