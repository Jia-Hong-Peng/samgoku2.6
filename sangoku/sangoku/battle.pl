
sub BATTLE_MODE{

	open(IN,"$DEF_LIST");
	@DEF_LIST3 = <IN>;
	close(IN);

	$d_hit=0;
	foreach(@DEF_LIST3){
		($did,$dname,$dtown_id,$dtown_flg,$dcon) = split(/<>/);
		if($cnum eq $dtown_id){
			$d_hit=1;last;
		}
	}


	&MAP_LOG("$xname國的$kname $zname進攻！");
	$eid="";
	if($d_hit){
		open(IN,"./charalog/main/$did.cgi") or &ERR2('帳號、密碼不正當！');
		@E_DATA = <IN>;
		close(IN);
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);
		$last_battle=0;
	}else{
		$ename = "城牆";
		$esol = $zshiro;
		$estr = 50;
		$egat = 50;
		$last_battle=1;
	}

	$win=0;
	open(IN,"./charalog/log/$kid\.cgi");
	@K_LOG2 = <IN>;
	close(IN);
	&K_LOG2("$xname國的$kname $zname進攻！");

	if($eid ne ""){
		open(IN,"./charalog/log/$eid\.cgi");
		@E_LOG2 = <IN>;
		close(IN);
		&E_LOG2("$xname國的$kname $ename戰鬥！");
	}

	&CHARA_ITEM_OPEN;

	$katt = int(($kstr + $karmdmg - int($egat / 5))/8);
	if($katt < 0){$katt = 0;}
	$eatt = int(($estr + $earmdmg - int($kgat / 5))/8);
	if($eatt < 0){$eatt = 0;}

	for($count=0;$count<99;$count++){
		$kdmg=0;
		$edmg=0;
		
		if($ksol <= 0){last;}
		$kdmg = int(rand($katt));
		if($kdmg <= 0){$kdmg=1;}
		$esol -= $kdmg;
		if($esol <= 0){
			$esol=0;
			&K_LOG2("回合<font color=red>$count</font>:$kname 兵士 $ksol人 ↓\(-$edmg\) |$ename 兵士 $esol人 ↓\(-$kdmg\)");
			&E_LOG2("回合<font color=red>$count</font>:$kname 兵士 $ksol人 ↓\(-$edmg\) |$ename 兵士 $esol人 ↓\(-$kdmg\)");
			$win = 1;last;
		}

		$edmg = int(rand($eatt));
		if($edmg <= 0){$edmg=1;}
		$ksol -= $edmg;
		if($ksol <= 0){
			$ksol=0;
			&K_LOG2("回合<font color=red>$count</font>:$kname 兵士 $ksol ↓\(-$edmg\) |$ename 兵士 $esol人 ↓\(-$kdmg\)");
			&E_LOG2("回合<font color=red>$count</font>:$kname 兵士 $ksol ↓\(-$edmg\) |$ename 兵士 $esol人 ↓\(-$kdmg\)");
			last;
		}
		&K_LOG2("回合<font color=red>$count</font>:$kname兵士$ksol ↓\(-$edmg\) |$ename 兵士 $esol人 ↓\(-$kdmg\)");
	}


	if($win){
		$ksub2_ex++;
		if($last_battle){
			&K_LOG2("<font color=red>$zname</font>入手。");
			if($town_get[$zcon] <= 1){
				@NEW_COU=();
				foreach(@COU_DATA){
					($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
					if("$zcon" eq "$xcid"){next;
					}else{
						push(@NEW_COU,"$_");
					}
				}
				open(OUT,">$COUNTRY_LIST") or &ERR('COUNTRY 不能寫上數據。');
				print OUT @NEW_COU;
				close(OUT);
				&MAP_LOG2("<font color=grey>【滅亡】</font>\[$old_date\]$cou_name[$zcon]國家滅亡。。");
				&MAP_LOG("<font color=grey>【滅亡】</font>\[$old_date\]$cou_name[$zcon]國家滅亡。。");
			}
				$zcon = $kcon;
				$znou = int($znou*0.8);
				$zsyo = int($zsyo*0.8);
				$znum = int($znum*0.9);
				$zpri = int($zpri*0.8);
				$kcex += 50;
				$kpos = $cnum;

				&MAP_LOG2("<font color=red>【支配】</font>\[$old_date\]$cou_name[$kcon]國的$kname $zname支配。");
				&MAP_LOG("<font color=red>【支配】</font>\[$old_date\]$cou_name[$kcon]國的$kname $zname支配。");
		}else{
			@NEW_DEF_LIST3=();
			foreach(@DEF_LIST3){
				($did,$dname,$dtown_id,$dtown_flg,$dcon) = split(/<>/);
				if($did eq $eid){
				}else{
					push(@NEW_DEF_LIST3,"$_");
				}
			}

			open(OUT,">$DEF_LIST");
			print OUT @NEW_DEF_LIST3;
			close(OUT);
			$kcex += 50;
			&K_LOG2("$kname $ename擊倒！");
			&E_LOG2("$ename $kname敗北。。");
			&MAP_LOG("<font color=red>【勝利】</font>$kname $ename擊倒！");
		}
	}else{
		&K_LOG2("$kname $ename敗北。。");
		&E_LOG2("$ename $kname擊倒！");
	}

	
	if($eid ne ""){
		&ENEMY_INPUT;
	}else{
		$zshiro = $esol;
		if("$zname" ne ""){
			splice(@TOWN_DATA,$cnum,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>\n");
		}
	}

	splice(@K_LOG2,20);

	open(OUT,">./charalog/log/$kid\.cgi");
	print OUT @K_LOG2;
	close(OUT);

	if($eid ne ""){
		splice(@E_LOG2,20);

		open(OUT,">./charalog/log/$eid\.cgi");
		print OUT @E_LOG2;
		close(OUT);
	}

}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/       　LOG 寫入　       _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub E_LOG2 {

	unshift(@E_LOG2,"$_[0]($mday日$hour時$min分)\n");
}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/       　LOG 寫入　       _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub K_LOG2 {

	unshift(@K_LOG2,"$_[0]($mday日$hour時$min分)\n");
}

1;

