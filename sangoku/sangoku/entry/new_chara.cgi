#_/_/_/_/_/_/_/_/_/_/_/_/#
#        NEW_CHARA       #
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub NEW_CHARA {

	&CHEACKER;
	if($CHARA_STOP){ &ERR2("�{�b�����s���a�n��"); }
	if ($in{'id'} =~ m/[^0-9a-zA-Z]/) {&E_ERR("�b�����t���b���^�Ʀr�H�~����r�C"); }
	if ($in{'pass'} =~ m/[^0-9a-zA-Z]/) {&E_ERR("�K�X���t���b���^�Ʀr�H�~����r�C"); }
	if ($in{'mail'} =~ /yahoo/ || $in{'mail'} =~ /hotmail/) {&E_ERR("���Ӷl��a�}����ϥΡC"); }
	if ($in{'mail'} eq "" || $in{'mail'} !~ /(.*)\@(.*)\.(.*)/){&E_ERR("�l�󪺿�J������C");}
	if($in{'id'} eq "" or length($in{'id'}) < 4 or length($in{'id'}) > 8) { &E_ERR("�b����J�A4�Ӧr�H�W�A8�Ӧr�H�U�C"); }
	elsif($in{'pass'} eq "" || length($in{'pass'}) < 4 || length($in{'pass'}) > 8) { &E_ERR("�K�X��J�A4�Ӧr�H�W�A8�Ӧr�H�U�C"); }
	elsif($in{'con'} eq "") { &E_ERR("�Q��ܪ����m�C"); }
	elsif($in{'mail'} eq "\@" || $in{'mail'} eq "") { &E_ERR("�l�󪺿�J������"); }
	elsif($in{'pass'} eq "" || length($in{'pass'}) < 4 || length($in{'pass'}) > 16) { &E_ERR("�n���H�����K�X�S���T���J�C"); }
	elsif($in{'chara_name'} eq "" || length($in{'chara_name'}) < 4 || length($in{'chara_name'}) > 12) { &E_ERR("�n���H�����W�r�S���T���J�C"); }
	elsif($in{'id'} eq $in{'pass'}){&E_ERR("�b���M�K�X�ۦP�A����n��"); }

	if ($in{'str'} =~ m/[^0-9]/){&E_ERR("�Z�O���t���Ʀr�H�~����r�C"); }
	if($in{'str'} eq "" || $in{'str'} < 5 || $in{'str'} > 100){&E_ERR("�Z�O�S����J�C");}

	if ($in{'int'} =~ m/[^0-9]/){&E_ERR("���O���t���Ʀr�H�~����r�C"); }
	if($in{'int'} eq "" || $in{'int'} < 5 || $in{'int'} > 100){&E_ERR("���O�S����J�C");}
	if ($in{'tou'} =~ m/[^0-9]/){&E_ERR("�βv�O���t���Ʀr�H�~����r�C"); }
	if ($in{'chara'} =~ m/[^0-9]/){&E_ERR("������C"); }
	if($in{'tou'} eq "" || $in{'tou'} < 5 || $in{'tou'} > 100){&E_ERR("�βv�O�S����J�C");}
	$max = $in{'str'} + $in{'int'} + $in{'tou'};
	if($max ne "150"){
		&E_ERR("��O�X�p�����O150�C(�p:$max)");
	}
	open(IN,"$TOWN_LIST") or &E_ERR("�����}���w�����C");
	@TOWN_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_LIST") or &E_ERR('�S�}���Cerr no :country');
	@COU_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_NO_LIST") or &E_ERR('�S�}���Cerr no :country no');
	@COU_NO_DATA = <IN>;
	close(IN);

	$zc=0;$m_hit=0;
	($z2name,$z2con)=split(/<>/,$TOWN_DATA[$in{'con'}]);
	if($z2con eq ""){
		if($in{'ele'} eq ""){
			&E_ERR("�п�ܧg�D����a�C��C");
		}elsif($in{'cou_name'} eq "" || length($in{'cou_name'}) < 2 || length($in{'cou_name'}) > 8) { &E_ERR("��a�W�٨S����J�C"); }
		$m_hit = 1;
		$cou_name = $in{'cou_name'};
		$new_cou_no = @COU_NO_DATA + 1;
		$hit = 1;
	}else{
		foreach(@COU_DATA){
			($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
			if($xcid eq $z2con){
				$cou_name = $xname;
				$kcon = $xcid;
				$hit = 1;
			}
		}
	}

	if(!$hit){
		&E_ERR("���Ӱ�a���s�b�C");
	}

	if($lockkey) { &F_LOCK; }

	&SET_COOKIE;
	&HOST_NAME;

	$date = time();
	$pos = 2;
	open(IN,"./charalog/main/$in{'id'}.cgi");
	@NEWCHARA = <IN>;
	close(IN);

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&E_ERR("�����}���C");
			}
			@page = <page>;
			close(page);
			push(@REGIST_VI,"@page<br>");
		}
	}
	closedir(dirlist);


	$hit=0;@new_chara=();
	($rkid,$rkpass,$rkname,$rkchara,$rkstr,$rkint,$rklea,$rkcha,$rksol,$rkgat,$rkcon,$rkgold,$rkrice,$rkcex,$rkclass,$rkarm,$rkbook,$rkbank,$rksub1,$rksub2,$rkpos,$rkmes,$rkhost,$rkdate,$rkmail,$rkos) = split(/<>/,$NEWCHARA[0]);

	if($rkid eq "$in{'id'}") {&E_ERR("���ӱb���w�g�n���F�C�п�ܨ�L�b���C");}

	if($REFREE){
		if($ENV{'HTTP_REFERER'} ne "$SANGOKU_URL/$FILE_ENTRY" && $ENV{'HTTP_REFERER'} ne "$SANGOKU_URL/$FILE_TOP" && $ENV{'HTTP_REFERER'} ne "$SANGOKU_URL/"){ &E_ERR("ERR No.001<BR>�n���H������@���C<BR>�ЦV�޲z�̬d�ߡC<BR>P1:$ROSER_URL/$FILE_ENTRY<BR>P2$ENV{'HTTP_REFERER'}"); }
	}
		foreach(@REGIST_VI){
			($rkid,$rkpass,$rkname,$rkchara,$rkstr,$rkint,$rklea,$rkcha,$rksol,$rkgat,$rkcon,$rkgold,$rkrice,$rkcex,$rkclass,$rkarm,$rkbook,$rkbank,$rksub1,$rksub2,$rkpos,$rkmes,$rkhost,$rkdate,$rkmail,$rkos) = split(/<>/);
			if($ACCESS){
				if($host eq $rkhost ){
					&E_ERR("�@�H�u��ϥΤ@�ӵn���H���C�ۦPIP�w�g�n���C");
				}
			}
			if($rkname eq "$in{'chara_name'}"){
				&E_ERR("�W�r�w�g�Q�n���C�ХΨ�L�W�r�n���C");
			}
			if($rkmail eq "$in{'mail'}"){
				&E_ERR("�l��a�}�w�g�Q�n���C");
			}
		}


	if($m_hit){
		$kcon = $new_cou_no;

		$month_read = "./withlove_sgklog/date_count.cgi";
		open(IN,"$month_read") or &E_ERR('�����}���C');
		@MONTH_DATA = <IN>;
		close(IN);
		($myear,$mmonth,$mtime) = split(/<>/,$MONTH_DATA[0]);
		$old_date = sprintf("%02d\�~%02d\��", $F_YEAR+$myear, $mmonth);

		push(@COU_DATA,"$new_cou_no<>$in{'cou_name'}<>$in{'ele'}<>1<>$in{'id'}<><>$in{'chara_name'}<>1<>\n");
		open(OUT,">$COUNTRY_LIST") or &E_ERR('COUNTRY ����g�J�ƾڡC');
		print OUT @COU_DATA;
		close(OUT);

		push(@COU_NO_DATA,"$new_cou_no<>$in{'cou_name'}<>$in{'ele'}<>1<>$in{'id'}<><><>1<>\n");
		open(OUT,">$COUNTRY_NO_LIST") or &E_ERR('COUNTRY ����g�J�ƾڡC');
		print OUT @COU_NO_DATA;
		close(OUT);

		&TOWN_DATA_OPEN("$in{'con'}");
		$zcon = $new_cou_no;
		&TOWN_DATA_INPUT;
		&MAP_LOG2("<font color=000088><B>�i�ذ�j</B></font>\[$old_date\] �s�g�D $in{'chara_name'} $cou_name �ذ�C");
		&MAP_LOG("<font color=000088><B>�i�ذ�j</B></font>�s�g�D $in{'chara_name'} $cou_name �ذ�C");

	}else{
		&MAP_LOG("<font color=0088CC><B>\[�K�x\]</B></font>�s�Z�N $in{'chara_name'} �b $cou_name ��K�x�C");
	}

	@NEW_COM=();
	for($i=0;$i<$MAX_COM;$i++){
		push(@NEW_COM,"<><><>$tt<><><>50<>\n");
	}

	open(OUT,">./charalog/command/$in{'id'}.cgi");
	print OUT @NEW_COM;
	close(OUT);

	if($ATTESTATION){
		&mail_to;
		$os = 0;
	}else{
		$os = 1;
	}

	$kcha = int(rand(101));
	$ksol = 0;
	$kgat = 0;
	$kgold = 1000;
	$krice = 500;
	$kcex = 0;
	$kclass = 0;
	$karm = 0;
	$kbook = 0;
	$kbank = "";
	$ksub1 = "";
	$ksub2 = $DEL_TURN - 10;
	$kstr = $in{'str'}+0;
	$kint = $in{'int'}+0;
	$ktou = $in{'tou'}+0;

	unshift(@new_chara,"$in{'id'}<>$in{'pass'}<>$in{'chara_name'}<>$in{'chara'}<>$kstr<>$kint<>$ktou<>$kcha<>$ksol<>$kgat<>$kcon<>$kgold<>$krice<>$kcex<>$kclass<>$karm<>$kbook<>$kbank<>$ksub1<>$ksub2<>$in{'con'}<>$in{'mes'}<>$host<>$date<>$in{'mail'}<>$os<>\n");

	open(OUT,">./charalog/main/$in{'id'}.cgi");
	print OUT @new_chara;
	close(OUT);



	if (-d $lockfile) { &UNLOCK_FILE; }
	&DATA_SEND;
	exit;
}


#------------------#
# �@�l��o�e�B�z�@ #
#------------------#
sub mail_to {
	$sendmail = '/usr/lib/sendmail';
	unless (-e $sendmail) { &E_ERR("sendmail ���o�e�����T"); }

	# �l����D
	$mail_sub = "Withlove�D�T���.Net �n�������q��";
	&TIME_DATA;

	$a_pass = crypt("$in{'pass'}", wd);
	# �l�󤺮e
	$mail_msg = <<"EOM";
$in{'chara_name'} �A�A�n�A

���§A�b $GAME_TITLE ���n���C
�A���n�����e�p�U�A�нT�{�C

���n������M�ɶ��G$daytime
���D���G$host
���Z�N�W�r�G$in{'chara_name'}
���q�l�l��G$in{'mail'}
���b���G$in{'id'}
���K�X�G$in{'pass'}
���{�ұK�X�G$a_pass

�{�ұK�X�n�����i�ѥ[�C���C

[�{�ұK�X���]�w]
$SANGOKU_URL/entry.cgi?mode=ATTESTATION
(���q�o��n���C)

�Х��\\Ū\�M���ѥ[�C�����W����A�}�l�C���C
�P�ɡA�b���αK�X�p�߰O�U�Φw���O�ޡC

_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/
$GAME_TITLE �޲z��
  Home:   $HOME_URL
EOM
	# �ܴ� JIS �s�X
    	#&jcode'convert(*mail_sub,'jis');
    	#&jcode'convert(*mail_msg,'jis');

	# �l�󤺪��t�_�@�檺�аO
	$mail_msg =~ s/<br>/\n/ig;

	# �l��B�z
	open(MAIL,"| $sendmail -t") || &E_ERR("�l��o�e����");
	print MAIL "To: $in{'mail'}\n";
	print MAIL "Subject: $mail_sub\n";
	print MAIL "MIME-Version: 1.0\n";
	print MAIL "Content-type: text/plain; charset=ISO-2022-JP\n";
	print MAIL "Content-Transfer-Encoding: 7bit\n";
	print MAIL "X-Mailer: $ver\n\n";
	print MAIL "$mail_msg\n";
	close(MAIL);

}
#_/_/_/_/_/_/_/_/#
#  ERROR PRINT   #
#_/_/_/_/_/_/_/_/#

sub E_ERR {

	&HEADER;
	if (-e $lockfile) { unlink($lockfile); }
	print "<center><hr size=0><h3>ERROR !</h3>\n";
	print "<P><font color=red><B>$_[0]</B></font>\n";
print "<form action=\"$FILE_ENTRY\" method=\"post\"><input type=hidden name=id value=$in{'id'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=mail value=$in{'mail'}><input type=hidden name=url value=$in{'url'}><input type=hidden name=chara_name value=$in{'chara_name'}><input type=hidden name=mes value=$in{'mes'}><input type=hidden name=mode value=entry><input type=submit value=\"��J��^\"></form>";
	print "<P><hr size=0></center>\n</body></html>\n";
	exit;
}
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/�@�@ �ѥ[�n���̤W���ֹ�@ �@_/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub CHEACKER {

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("�����}���!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);


	$num = @CL_DATA;

	if($ENTRY_MAX){
		if($num > $ENTRY_MAX){
			&ERR2("�W�X�̤j�n����\[$ENTRY_MAX\]�C�������s���a�n���C");
		}
	}
}

1;