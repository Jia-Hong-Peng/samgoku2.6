#_/_/_/_/_/_/_/_/_/_/#
#　　　　登用２　　　#
#_/_/_/_/_/_/_/_/_/_/#

sub GET_MAN2 {

	if($in{'no'} eq ""){&ERR("NO:沒有輸入。");}
	if($in{'num'} eq ""){&ERR("沒有輸入對手。");}
	if(length($in{'mes'}) > 120) { &ERR("信，請以全角60個字以下輸入。"); }

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);
	if($kgold < 100){&ERR("金不足夠。");}

	$num = $in{'num'};
	$hit=0;

	open(IN,"./charalog/main/$num\.cgi") or &ERR('不能登用。');
	@E_DATA = <IN>;
	close(IN);
	($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);


	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	$add_mes = "$xname國家的使者";

	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
				push(@NEW_COM_DATA,"$in{'mode'}<>$ename<>$ename登用<>9999<>$add_mes:$in{'mes'}<>$in{'num'}<>$kcon<>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);
			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"$in{'mode'}<>$ename<>$ename登用<>9999<>$add_mes:$in{'mes'}<>$in{'num'}<>$kcon<>\n");
					$lno = $_ + 1;
					$no .= "$lno,";
				}
			}
			if(!$ahit){
				push(@NEW_COM_DATA,"$_");
			}
			$i++;
		}
	}
	open(OUT,">./charalog/command/$kid.cgi") or &ERR('打不開文件。');
	print OUT @NEW_COM_DATA;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">NO:$no $ename登用輸入。</font></h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="確定"></form></CENTER><center>
EOM

	&FOOTER;

	exit;

}
1;