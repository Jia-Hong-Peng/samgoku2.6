#_/_/_/_/_/_/_/_/_/_/#
#　　　 購入２ 　　　#
#_/_/_/_/_/_/_/_/_/_/#

sub ARM_BUY2 {

	if($in{'no'} eq ""){&ERR("NO:沒有輸入。");}
	if($in{'select'} eq ""){&ERR("沒有輸入商品。");}
	&CHARA_MAIN_OPEN;
	open(IN,"$ARM_LIST") or &ERR('打不開文件。');
	@ARM_DATA = <IN>;
	close(IN);

	$num = $in{'select'};
	($earmname,$earmval,$earmdmg,$earmwei,$earmele,$earmsta,$earmclass,$earmtownid) = split(/<>/,$ARM_DATA[$num]);
	$hit=0;
	if($earmval > $kgold){&ERR("金不足夠。");}

	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	@NEW_COM_DATA=();$i=0;

	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
			push(@NEW_COM_DATA,"$in{'mode'}<><>武器:$earmname 購入<>$tt<><>$num<><>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);
			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"$in{'mode'}<><>武器:$earmname 購入<>$tt<><>$num<><>\n");
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
<CENTER><hr size=0><h2><font color="#FFFFFF">NO:$no ;武器:$earmname 購入輸入。</font></h2><p>
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