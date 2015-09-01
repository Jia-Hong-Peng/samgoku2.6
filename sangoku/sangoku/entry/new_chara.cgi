#_/_/_/_/_/_/_/_/_/_/_/_/#
#        NEW_CHARA       #
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub NEW_CHARA {

	&CHEACKER;
	if($CHARA_STOP){ &ERR2("現在不接新玩家登錄"); }
	if ($in{'id'} =~ m/[^0-9a-zA-Z]/) {&E_ERR("帳號中含有半角英數字以外的文字。"); }
	if ($in{'pass'} =~ m/[^0-9a-zA-Z]/) {&E_ERR("密碼中含有半角英數字以外的文字。"); }
	if ($in{'mail'} =~ /yahoo/ || $in{'mail'} =~ /hotmail/) {&E_ERR("那個郵件地址不能使用。"); }
	if ($in{'mail'} eq "" || $in{'mail'} !~ /(.*)\@(.*)\.(.*)/){&E_ERR("郵件的輸入不正當。");}
	if($in{'id'} eq "" or length($in{'id'}) < 4 or length($in{'id'}) > 8) { &E_ERR("帳號輸入，4個字以上，8個字以下。"); }
	elsif($in{'pass'} eq "" || length($in{'pass'}) < 4 || length($in{'pass'}) > 8) { &E_ERR("密碼輸入，4個字以上，8個字以下。"); }
	elsif($in{'con'} eq "") { &E_ERR("被選擇初期位置。"); }
	elsif($in{'mail'} eq "\@" || $in{'mail'} eq "") { &E_ERR("郵件的輸入不正當"); }
	elsif($in{'pass'} eq "" || length($in{'pass'}) < 4 || length($in{'pass'}) > 16) { &E_ERR("登場人物的密碼沒有確實輸入。"); }
	elsif($in{'chara_name'} eq "" || length($in{'chara_name'}) < 4 || length($in{'chara_name'}) > 12) { &E_ERR("登場人物的名字沒有確實輸入。"); }
	elsif($in{'id'} eq $in{'pass'}){&E_ERR("帳號和密碼相同，不能登錄"); }

	if ($in{'str'} =~ m/[^0-9]/){&E_ERR("武力中含有數字以外的文字。"); }
	if($in{'str'} eq "" || $in{'str'} < 5 || $in{'str'} > 100){&E_ERR("武力沒有輸入。");}

	if ($in{'int'} =~ m/[^0-9]/){&E_ERR("知力中含有數字以外的文字。"); }
	if($in{'int'} eq "" || $in{'int'} < 5 || $in{'int'} > 100){&E_ERR("知力沒有輸入。");}
	if ($in{'tou'} =~ m/[^0-9]/){&E_ERR("統率力中含有數字以外的文字。"); }
	if ($in{'chara'} =~ m/[^0-9]/){&E_ERR("不正當。"); }
	if($in{'tou'} eq "" || $in{'tou'} < 5 || $in{'tou'} > 100){&E_ERR("統率力沒有輸入。");}
	$max = $in{'str'} + $in{'int'} + $in{'tou'};
	if($max ne "150"){
		&E_ERR("能力合計必須是150。(計:$max)");
	}
	open(IN,"$TOWN_LIST") or &E_ERR("打不開指定的文件。");
	@TOWN_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_LIST") or &E_ERR('沒開文件。err no :country');
	@COU_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_NO_LIST") or &E_ERR('沒開文件。err no :country no');
	@COU_NO_DATA = <IN>;
	close(IN);

	$zc=0;$m_hit=0;
	($z2name,$z2con)=split(/<>/,$TOWN_DATA[$in{'con'}]);
	if($z2con eq ""){
		if($in{'ele'} eq ""){
			&E_ERR("請選擇君主的國家顏色。");
		}elsif($in{'cou_name'} eq "" || length($in{'cou_name'}) < 2 || length($in{'cou_name'}) > 8) { &E_ERR("國家名稱沒有輸入。"); }
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
		&E_ERR("那個國家不存在。");
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
				&E_ERR("打不開文件。");
			}
			@page = <page>;
			close(page);
			push(@REGIST_VI,"@page<br>");
		}
	}
	closedir(dirlist);


	$hit=0;@new_chara=();
	($rkid,$rkpass,$rkname,$rkchara,$rkstr,$rkint,$rklea,$rkcha,$rksol,$rkgat,$rkcon,$rkgold,$rkrice,$rkcex,$rkclass,$rkarm,$rkbook,$rkbank,$rksub1,$rksub2,$rkpos,$rkmes,$rkhost,$rkdate,$rkmail,$rkos) = split(/<>/,$NEWCHARA[0]);

	if($rkid eq "$in{'id'}") {&E_ERR("那個帳號已經登錄了。請選擇其他帳號。");}

	if($REFREE){
		if($ENV{'HTTP_REFERER'} ne "$SANGOKU_URL/$FILE_ENTRY" && $ENV{'HTTP_REFERER'} ne "$SANGOKU_URL/$FILE_TOP" && $ENV{'HTTP_REFERER'} ne "$SANGOKU_URL/"){ &E_ERR("ERR No.001<BR>登場人物不能作成。<BR>請向管理者查詢。<BR>P1:$ROSER_URL/$FILE_ENTRY<BR>P2$ENV{'HTTP_REFERER'}"); }
	}
		foreach(@REGIST_VI){
			($rkid,$rkpass,$rkname,$rkchara,$rkstr,$rkint,$rklea,$rkcha,$rksol,$rkgat,$rkcon,$rkgold,$rkrice,$rkcex,$rkclass,$rkarm,$rkbook,$rkbank,$rksub1,$rksub2,$rkpos,$rkmes,$rkhost,$rkdate,$rkmail,$rkos) = split(/<>/);
			if($ACCESS){
				if($host eq $rkhost ){
					&E_ERR("一人只能使用一個登場人物。相同IP已經登錄。");
				}
			}
			if($rkname eq "$in{'chara_name'}"){
				&E_ERR("名字已經被登錄。請用其他名字登錄。");
			}
			if($rkmail eq "$in{'mail'}"){
				&E_ERR("郵件地址已經被登錄。");
			}
		}


	if($m_hit){
		$kcon = $new_cou_no;

		$month_read = "./withlove_sgklog/date_count.cgi";
		open(IN,"$month_read") or &E_ERR('打不開文件。');
		@MONTH_DATA = <IN>;
		close(IN);
		($myear,$mmonth,$mtime) = split(/<>/,$MONTH_DATA[0]);
		$old_date = sprintf("%02d\年%02d\月", $F_YEAR+$myear, $mmonth);

		push(@COU_DATA,"$new_cou_no<>$in{'cou_name'}<>$in{'ele'}<>1<>$in{'id'}<><>$in{'chara_name'}<>1<>\n");
		open(OUT,">$COUNTRY_LIST") or &E_ERR('COUNTRY 不能寫入數據。');
		print OUT @COU_DATA;
		close(OUT);

		push(@COU_NO_DATA,"$new_cou_no<>$in{'cou_name'}<>$in{'ele'}<>1<>$in{'id'}<><><>1<>\n");
		open(OUT,">$COUNTRY_NO_LIST") or &E_ERR('COUNTRY 不能寫入數據。');
		print OUT @COU_NO_DATA;
		close(OUT);

		&TOWN_DATA_OPEN("$in{'con'}");
		$zcon = $new_cou_no;
		&TOWN_DATA_INPUT;
		&MAP_LOG2("<font color=000088><B>【建國】</B></font>\[$old_date\] 新君主 $in{'chara_name'} $cou_name 建國。");
		&MAP_LOG("<font color=000088><B>【建國】</B></font>新君主 $in{'chara_name'} $cou_name 建國。");

	}else{
		&MAP_LOG("<font color=0088CC><B>\[仕官\]</B></font>新武將 $in{'chara_name'} 在 $cou_name 國仕官。");
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
# 　郵件發送處理　 #
#------------------#
sub mail_to {
	$sendmail = '/usr/lib/sendmail';
	unless (-e $sendmail) { &E_ERR("sendmail 的發送不正確"); }

	# 郵件標題
	$mail_sub = "Withlove．三國志.Net 登錄完成通知";
	&TIME_DATA;

	$a_pass = crypt("$in{'pass'}", wd);
	# 郵件內容
	$mail_msg = <<"EOM";
$in{'chara_name'} ，你好，

謝謝你在 $GAME_TITLE 的登錄。
你的登錄內容如下，請確認。

■登錄日期和時間：$daytime
■主機：$host
■武將名字：$in{'chara_name'}
■電子郵件：$in{'mail'}
■帳號：$in{'id'}
■密碼：$in{'pass'}
■認證密碼：$a_pass

認證密碼登錄後方可參加遊戲。

[認證密碼的設定]
$SANGOKU_URL/entry.cgi?mode=ATTESTATION
(※從這邊登錄。)

請先閱\讀\清楚參加遊戲的規章後再開始遊戲。
同時，帳號及密碼小心記下及安全保管。

_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/
$GAME_TITLE 管理員
  Home:   $HOME_URL
EOM
	# 變換 JIS 編碼
    	#&jcode'convert(*mail_sub,'jis');
    	#&jcode'convert(*mail_msg,'jis');

	# 郵件內的另起一行的標記
	$mail_msg =~ s/<br>/\n/ig;

	# 郵件處理
	open(MAIL,"| $sendmail -t") || &E_ERR("郵件發送失敗");
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
print "<form action=\"$FILE_ENTRY\" method=\"post\"><input type=hidden name=id value=$in{'id'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=mail value=$in{'mail'}><input type=hidden name=url value=$in{'url'}><input type=hidden name=chara_name value=$in{'chara_name'}><input type=hidden name=mes value=$in{'mes'}><input type=hidden name=mode value=entry><input type=submit value=\"輸入返回\"></form>";
	print "<P><hr size=0></center>\n</body></html>\n";
	exit;
}
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/　　 參加登錄者上限核對　 　_/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub CHEACKER {

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("打不開文件!");
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
			&ERR2("超出最大登錄數\[$ENTRY_MAX\]。不接受新玩家登錄。");
		}
	}
}

1;