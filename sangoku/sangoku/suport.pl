#_/_/_/_/_/_/_/_/_/_/_/_/#
#   CHARA MAIN OPEN      #
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub CHARA_MAIN_OPEN {

	open(IN,"./charalog/main/$in{'id'}.cgi") or &ERR2('¨S¦³³o­Ó±b¸¹¡I');
	@CN_DATA = <IN>;
	close(IN);

	($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/,$CN_DATA[0]);

	if($in{'id'} ne "$kid" or $in{'pass'} ne "$kpass"){&ERR2("¨S¦³³o­Ó±b¸¹¡I");}

}

#_/_/_/_/_/_/_/_/_/_/_/_/#
#   CHARA MAIN INPUT     #
#_/_/_/_/_/_/_/_/_/_/_/_/#
sub CHARA_MAIN_INPUT {

	@NEW_DATA=();
	unshift(@NEW_DATA,"$kid<>$kpass<>$kname<>$kchara<>$kstr<>$kint<>$klea<>$kcha<>$ksol<>$kgat<>$kcon<>$kgold<>$krice<>$kcex<>$kclass<>$karm<>$kbook<>$kbank<>$ksub1<>$ksub2<>$kpos<>$kmes<>$khost<>$kdate<>$kmail<>$kos<>\n");
	open(OUT,">./charalog/main/$kid\.cgi") or &ERR('MAIN ¤£¯à¼g¤W·sªº¼Æ¾Ú¡C');
	print OUT @NEW_DATA;
	close(OUT);

}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#     ENEMY DATA ALL OPEN      #
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub ENEMY_OPEN {

	open(IN,"./charalog/main/$in{'eid'}.cgi") or &ERR2('±b¸¹©Î±K½X¿ù»~¡I');
	@E_DATA = <IN>;
	close(IN);
	($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);
	if($in{'eid'} ne "$eid" ){&ERR2("±b¸¹©Î±K½X¿ù»~¡I");}

}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#    ENEMY DATA ALL INPUT      #
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
sub ENEMY_INPUT {

	@NEW_DATA=();
	unshift(@NEW_DATA,"$eid<>$epass<>$ename<>$echara<>$estr<>$eint<>$elea<>$echa<>$esol<>$egat<>$econ<>$egold<>$erice<>$ecex<>$eclass<>$earm<>$ebook<>$ebank<>$esub1<>$esub2<>$epos<>$emes<>$ehost<>$edate<>$email<>$eos<>\n");
	open(OUT,">./charalog/main/$eid\.cgi") or &ERR2('ENEMY ¤£¯à¼g¤W·sªº¼Æ¾Ú¡C');
	print OUT @NEW_DATA;
	close(OUT);

}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/        LOGªº¼g¤J ‚Ý      _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub MAP_LOG {

	if($lockkey) { &F_LOCK; }
	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	&TIME_DATA;

	unshift(@S_MOVE,"$_[0]($mday¤é$hour®É$min¤À)\n");

	splice(@S_MOVE,20);

	open(OUT,">$MAP_LOG_LIST") or &ERR2('LOG ¤£¯à¼g¤W·sªº¼Æ¾Ú¡C');
	print OUT @S_MOVE;
	close(OUT);
	if (-d $lockfile) { &UNLOCK_FILE; }

}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/        LOGªº¼g¤J ‚Ý      _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub MAP_LOG2 {

	if($lockkey) { &F_LOCK; }
	open(IN,"$MAP_LOG_LIST2");
	@S_MOVE = <IN>;
	close(IN);

	unshift(@S_MOVE,"<b>$_[0]</b>($mday¤é$hour®É$min¤À)\n");

	splice(@S_MOVE,20);

	open(OUT,">$MAP_LOG_LIST2") or &ERR2('LOG ¤£¯à¼g¤W·sªº¼Æ¾Ú¡C');
	print OUT @S_MOVE;
	close(OUT);
	if (-d $lockfile) { &UNLOCK_FILE; }

}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/        LOGªº¼g¤J‚Ý       _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub K_LOG {

	open(IN,"./charalog/log/$kid.cgi");
	@K_LOG = <IN>;
	close(IN);

	unshift(@K_LOG,"$_[0]($mday¤é$hour®É$min¤À)\n");

	splice(@K_LOG,20);

	open(OUT,">./charalog/log/$kid.cgi");
	print OUT @K_LOG;
	close(OUT);

}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#    BATTLE ITEM ALL OPEN      #
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub CHARA_ITEM_OPEN {

	open(IN,"$ARM_LIST") or &ERR('¥´¤£¶}¤å¥ó¡C');
	@ARM_DATA = <IN>;
	close(IN);
	open(IN,"$PRO_LIST") or &ERR('¥´¤£¶}¤å¥ó¡C');
	@PRO_DATA = <IN>;
	close(IN);

	($karmname,$karmval,$karmdmg,$karmwei,$karmele,$karmsta,$karmclass,$karmtownid) = split(/<>/,$ARM_DATA[$karm]);
	($kproname,$kproval,$kprodmg,$kprowei,$kproele,$kprosta,$kproclass,$kprotownid) = split(/<>/,$PRO_DATA[$kbook]);

	if($eid){
		($earmname,$earmval,$earmdmg,$earmwei,$earmele,$earmsta,$earmclass,$earmtownid) = split(/<>/,$ARM_DATA[$earm]);
		($eproname,$eproval,$eprodmg,$eprowei,$eproele,$eprosta,$eproclass,$eprotownid) = split(/<>/,$PRO_DATA[$ebook]);
	}

}

#_/_/_/_/_/_/_/_/_/_/_/_/#
#¡@¡@¡@¡@®É¶¡¨ú±o¡@¡@¡@¡@#
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub TIME_DATA {
	$tt = time ;
	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime(time);
	$mon++;
	$ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
	$daytime = sprintf("%02d\/%02d\/(%s) %02d:%02d", $mon,$mday,$ww,$hour,$min);
}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#        COUNTRY DATA OPEN       #
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub COUNTRY_DATA_OPEN {

	open(IN,"$COUNTRY_LIST") or &ERR2('¨S¶}¤å¥ó¡Cerr no :country');
	@COU_DATA = <IN>;
	close(IN);
	$country_no=0;$hit=0;
	foreach(@COU_DATA){
		($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
		if("$_[0]" eq "$xcid"){$hit=1;last;}
		$country_no++;
	}

	if(!$hit){
		$xcid=0;
		$xname="µL©ÒÄÝ";
		$xele=0;
		$xmark=0;
		$xking="";
		$xmes=0;
		$xsub=0;
		$xpri=0;
	}
	($xgunshi,$xdai,$xuma,$xgoei,$xyumi,$xhei,$xxsub1,$xxsub2)= split(/,/,$xsub);

	foreach(@COU_DATA){
		($x2cid,$x2name,$x2ele,$x2mark)=split(/<>/);
		$cou_name[$x2cid] = "$x2name";
		$cou_ele[$x2cid] = "$x2ele";
		$cou_mark[$x2cid] = "$x2mark";
	}
}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#      COUNTRY DATA INPUT      #
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
sub COUNTRY_DATA_INPUT {

	if($lockkey) { &F_LOCK; }

	if("$xcid" ne "0" && "$xcid" ne ""){
		splice(@COU_DATA,$country_no,1,"$xcid<>$xname<>$xele<>$xmark<>$xking<>$xmes<>$xsub<>$xpri<>\n");
		open(OUT,">$COUNTRY_LIST") or &ERR('COUNTRY ¤£¯à¼g¤W¼Æ¾Ú¡C');
		print OUT @COU_DATA;
		close(OUT);
	}

	$s_i = int(rand(5));
	if($s_i eq "0" && $xcid ne ""){
		open(OUT,">$COUNTRY_LIST2") or &ERR('COUNTRY2 ¤£¯à¼g¤W·sªº¼Æ¾Ú¡C');
		print OUT @COU_DATA;
		close(OUT);
	}
	if (-d $lockfile) { &UNLOCK_FILE; }

}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#        TOWN DATA OPEN          #
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub TOWN_DATA_OPEN {

	open(IN,"$TOWN_LIST") or &ERR("¥´¤£¶}«ü©wªº¤å¥ó¡C");
	@TOWN_DATA = <IN>;
	close(IN);
	$zid = $_[0];
	($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7])=split(/<>/,$TOWN_DATA[$_[0]]);

	if($zname eq ""){&ERR("³o­Ó³£¥«¤£¦s¦b¡C");}

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

}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#       TOWN DATA INPUT        #
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
sub TOWN_DATA_INPUT {

	if($lockkey) { &F_LOCK; }

	if("$zname" ne ""){
		splice(@TOWN_DATA,$zid,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
		open(OUT,">$TOWN_LIST") or &ERR('TOWN ¤£¯à¼g¤W¼Æ¾Ú¡C');
		print OUT @TOWN_DATA;
		close(OUT);
	}

	$s_it = int(rand(3));
	if($s_it eq "0" && $zname ne ""){
		open(OUT,">$TOWN_LIST2") or &ERR('TOWN2 ¤£¯à¼g¤W·sªº¼Æ¾Ú¡C');
		print OUT @TOWN_DATA;
		close(OUT);
	}
	if (-d $lockfile) { &UNLOCK_FILE; }
}

#_/_/_/_/_/_/_/_/#
#     DECODE     #
#_/_/_/_/_/_/_/_/#

sub DECODE {

	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		if ($ENV{'CONTENT_LENGTH'} > 51200) { &ERR("§ë½Z¶q¤Ó¤j"); }
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	} else { $buffer = $ENV{'QUERY_STRING'}; }
	@pairs = split(/&/, $buffer);

	$v=0;
	foreach (@pairs) {
		($name,$value) = split(/=/, $_);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

		# ÅÜ´«¦r²Å½s½X - JIS
		#&jcode'convert(*value, "sjis", "", "z");

		# ¼Ð°O³B²z
		$value =~ s/</&lt;/g;
		$value =~ s/>/&gt;/g;
		$value =~ s/\"/&quot;/g;


		# ¹j¦æ³B²z
		if ($name eq "ins") {
			$value =~ s/\r\n/<br>/g;
			$value =~ s/\r/<br>/g;
			$value =~ s/\n/<br>/g;
		} else {
			$value =~ s/\r//g;
			$value =~ s/\n//g;
		}

		if($name eq 'no'){
			$no[$v] = $value;
			$v++;
			$in{$name} = $value;
		}else{
			$in{$name} = $value;
		}
	}
	$mode = $in{'mode'};
	$in{'url'} =~ s/^http\:\/\///;
	$cookie_pass = $in{'pass'};
	$cookie_id = $in{'id'};
}


#_/_/_/_/_/_/_/_/#
#   HOST NAME    #
#_/_/_/_/_/_/_/_/#

sub HOST_NAME {
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};

	if ($get_remotehost) {
		if ($host eq "" || $host eq "$addr") {
			$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2);
		}
	}
	if ($host eq "") { $host = $addr; }


}

#_/_/_/_/_/_/_/_/#
#  ERROR PRINT   #
#_/_/_/_/_/_/_/_/#

sub ERR {

	&CHARA_MAIN_OPEN;
	&HEADER;
	if (-d $lockfile) { &UNLOCK_FILE; }
	print "<center><hr size=0><h3>ERROR !</h3>\n";
	print "<P><font color=red><B>$_[0]</B></font>\n";
print "<form action=\"$FILE_STATUS\" method=\"post\"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=STATUS><input type=submit value=\"ªð¦^³£¥«\"></form>";
	print "<P><hr size=0></center>\n</body></html>\n";
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#   ERROR PRINT2   #
#_/_/_/_/_/_/_/_/_/#

sub ERR2 {

	&HEADER;
	if (-d $lockfile) { &UNLOCK_FILE; }
	print "<center><hr size=0><h3>ERROR !</h3>\n";
	print "<P><font color=red><B>$_[0]</B></font>\n";
	print "<P><hr size=0></center>\n</body></html>\n";
	exit;
}

#_/_/_/_/_/_/_/_/_/_/_/_/#
#       FILE LOCK        #
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub F_LOCK {

	$qhit=0;
	for($qp=0;$qp<1;$qp++){
		if (-d $lockfile) {
			$qhit=1;
			sleep(1);
			last;
 		}else{
			mkdir($lockfile, 0755);
		}
	}

	if($qhit){
     	&UNLOCK_FILE();
	 	&ERR("File lock error!<BR>¼Æ¾Ú§ó·s¤¤¡C½Ðµy«á¦A¸Õ¡C");
	}

}

#_/_/_/_/_/_/_/_/_/_/_/_/#
#     FILE UNLOCK        #
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub UNLOCK_FILE
{
  rmdir("$lockfile");
}

#_/_/_/_/_/_/_/_/_/_/_/_/#
#       HTML HEADER      #
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub HEADER {

	print "Cache-Control: no-cache\n";
	print "Pragma: no-cache\n";
	print "Content-type: text/html\n\n";
	print <<"EOM";
<html>
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=big5">
EOM
	print <<"EOM";
<STYLE type="text/css">
<!--
BODY,TR,TD,TH{
font-family : "·s²Ó©úÅé";
font-size: $FONT_SIZE
}
A:HOVER{
 color: $ALINK
}
.S1 {color:#fff; border-style: double; border-width: 3px;BACKGROUND: #633;}
.dmg { color: #FF0000; font-size: 18pt }
.clit { color: #0000FF; font-size: 18pt }
.r { color: #FF4444; font-size: 10pt }
.b { color: #4444DD; font-size: 10pt }
.s { color: #44AAEE; font-size: 10pt }
.g { color: #44DD44; font-size: 10pt }
.o { color: #EEAA44; font-size: 10pt }
-->
</STYLE>
<title>$GAME_TITLE</title></head>
<body background="$BACKGROUND" bgcolor="$BGCOLOR" text="$TEXT" link="$LINK" vlink="$VLINK" alink="$ALINK" leftmargin="0" marginwidth="0" marginheight="0">
EOM


}

#_/_/_/_/_/_/_/_/_/_/_/_/#
#       HTML FOOTER      #
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub FOOTER {
	# ¥i§ïÅÜ¡A¦ý¸T¤î§R°£
	print "<HR SIZE=0>\n";
	print "<font color=#FFFFFF>¤T°ê§Ó.NET $VER </font><a href=\"http://www3.to/maccyu2/\" target=\"_blank\">maccyu</a><br>\n";
	print "<font color=#FFFFFF>¹CÀ¸Ác¤Æ¤Î¬ü¤Æ </font><a href=\"http://withlove.no-ip.com/\" target=\"_blank\">Withlove -- ¹Ú¤Û¾Ç¶é¡DYouko</a><br>\n";
	print "<font color=#FFFFFF>ºô­¶±H¦s </font><a href=\"http://wlserver.net/\" target=\"_blank\">WLserver Network Services</a><br>\n";
	print "<font color=#FFFFFF>ADMINISTARTOR </font><a href=\"./index.cgi\" target=\"_top\">HOME</a><br>\n";
    print "</body></html>\n";
}

#_/_/_/_/_/_/_/_/_/_/_/_/#
#    COOKIE ±¡³ø¨ú±o¡@ ¡@#
#_/_/_/_/_/_/_/_/_/_/_/_/#
sub GET_COOKIE {
	@pairs = split(/;/, $ENV{'HTTP_COOKIE'});
	foreach (@pairs) {
		local($key,$val) = split(/=/);
		$key =~ s/\s//g;
		$GET{$key} = $val;
	}
	@pairs = split(/,/, $GET{'WOR'});
	foreach (@pairs) {
		local($key,$val) = split(/<>/);
		$COOK{$key} = $val;
	}
	$_id  = $COOK{'id'};
	$_pass = $COOK{'pass'};
}

#_/_/_/_/_/_/_/_/_/_/_/_/#
#        SET COOKIE      #
#_/_/_/_/_/_/_/_/_/_/_/_/#
sub SET_COOKIE {

	local($sec,$min,$hour,$mday,$mon,$year,$wday) = gmtime(time+60*24*60*60);
	@month=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');
	$gmt = sprintf("%s, %02d-%s-%04d %02d:%02d:%02d GMT",
			$week[$wday],$mday,$month[$mon],$year+1900,$hour,$min,$sec);
	$cook="id<>$cookie_id\,pass<>$cookie_pass";
	print "Set-Cookie: WOR=$cook; expires=$gmt\n";
}

#_/_/_/_/_/_/_/_/_/_/#
#   GUEST ±¡³ø¦¬¶° ¡@#
#_/_/_/_/_/_/_/_/_/_/#

sub MAKE_GUEST_LIST {

	if($lockkey) { &F_LOCK; }
	open(GUEST,"$GUEST_LIST") or &ERR2('¥´¤£¶}¤å¥ó¡C');
	@GUEST=<GUEST>;close(GUEST);

	$times = time();@m_list = ();$hit=0;@New_guest_list=();

	foreach (@GUEST){($timer,$name,$con,$opos) = split(/<>/);
		if( $times - 180 > $timer){
			next;
		}elsif($kname eq $name){
			if( $times - 5 <= $timer){ &ERR("½Ð¤Å¦P®É³sÄò§ó·s¡C<BR>»P«e¦^§ó·s¥²¶·¬Û¹j³Ì¤Ö¢´¬í¡C"); }
			push (@New_guest_list,"$times<>$kname<>$kcon<>$kpos<>\n");
			$m_list .= "$kname\[$town_name[$kpos]\] ";
			$hit = 1;
		}else{
			push (@New_guest_list,"$timer<>$name<>$con<>$opos<>\n");
			if($kcon eq $con){
				$m_list .= "$name\[$town_name[$opos]\] ";
			}
		}
	}

	if(!$hit){
		push(@New_guest_list,"$times<>$kname<>$kcon<>$kpos<>\n");
		$m_list .= "$kname\[$town_name[$kpos]\] ";
	}

	open(GUEST,">$GUEST_LIST") or &ERR('¥´¤£¶}¤å¥ó¡C');
	print GUEST @New_guest_list;close(GUEST);
	if (-d $lockfile) { &UNLOCK_FILE; }
}

#_/_/_/_/_/_/_/_/_/_/#
#¡@¡@­t²ü¨¾¤î¾÷¯à¡@¡@#
#_/_/_/_/_/_/_/_/_/_/#

sub SERVER_STOP {

	&HOST_NAME;
	open(GUEST,"./withlove_sgklog/stop.cgi") or &ERR2('¥´¤£¶}¤å¥ó¡C');
	@STOP=<GUEST>;close(GUEST);
if($host eq ""){&ERR("¥D¾÷¦WºÙµL®Ä¡C");}
	$times = time();@m_list = ();$hit=0;@New_stop=();
	$phit=0;
	foreach (@STOP){
		($stimer,$shost) = split(/<>/);
		if( $times - 180 > $stimer){
			next;
		}elsif($shost eq $host){
			if( $times-5 <= $stimer){
				$phit = 1;
			}
			push (@New_stop,"$times<>$host<>\n");
			$hit = 1;
		}else{
			push (@New_stop,"$stimer<>$shost<>\n");
		}
	}


	if(!$hit){
		push(@New_stop,"$times<>$host<>\n");
	}

	open(GUEST,">./withlove_sgklog/stop.cgi") or &ERR('¥´¤£¶}¤å¥ó¡C');
	print GUEST @New_stop;close(GUEST);

	if($phit){
		if($in{'id'} eq ""){
#			&ERR2("¨¾¤î¦øªA¾¹­t²ü¶q¹L­«¡A§ó·s¤§«á<BR>½Ð¬Û¹j³Ì¤Ö¢´¬í¦A°õ¦æ§ó·s¡C<BR>§Aªº¥D¾÷¦WºÙ¡G$host"); 
		}else{
#			&ERR("¨¾¤î¦øªA¾¹­t²ü¶q¹L­«¡A§ó·s¤§«á<BR>½Ð¬Û¹j³Ì¤Ö¢´¬í¦A°õ¦æ§ó·s¡C<BR>§Aªº¥D¾÷¦WºÙ¡G$host"); 
		}
	}

}


1;

