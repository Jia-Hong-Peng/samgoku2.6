
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


	&MAP_LOG("$xname�ꪺ$kname $zname�i��I");
	$eid="";
	if($d_hit){
		open(IN,"./charalog/main/$did.cgi") or &ERR2('�b���B�K�X������I');
		@E_DATA = <IN>;
		close(IN);
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);
		$last_battle=0;
	}else{
		$ename = "����";
		$esol = $zshiro;
		$estr = 50;
		$egat = 50;
		$last_battle=1;
	}

	$win=0;
	open(IN,"./charalog/log/$kid\.cgi");
	@K_LOG2 = <IN>;
	close(IN);
	&K_LOG2("$xname�ꪺ$kname $zname�i��I");

	if($eid ne ""){
		open(IN,"./charalog/log/$eid\.cgi");
		@E_LOG2 = <IN>;
		close(IN);
		&E_LOG2("$xname�ꪺ$kname $ename�԰��I");
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
			&K_LOG2("�^�X<font color=red>$count</font>:$kname �L�h $ksol�H ��\(-$edmg\) |$ename �L�h $esol�H ��\(-$kdmg\)");
			&E_LOG2("�^�X<font color=red>$count</font>:$kname �L�h $ksol�H ��\(-$edmg\) |$ename �L�h $esol�H ��\(-$kdmg\)");
			$win = 1;last;
		}

		$edmg = int(rand($eatt));
		if($edmg <= 0){$edmg=1;}
		$ksol -= $edmg;
		if($ksol <= 0){
			$ksol=0;
			&K_LOG2("�^�X<font color=red>$count</font>:$kname �L�h $ksol ��\(-$edmg\) |$ename �L�h $esol�H ��\(-$kdmg\)");
			&E_LOG2("�^�X<font color=red>$count</font>:$kname �L�h $ksol ��\(-$edmg\) |$ename �L�h $esol�H ��\(-$kdmg\)");
			last;
		}
		&K_LOG2("�^�X<font color=red>$count</font>:$kname�L�h$ksol ��\(-$edmg\) |$ename �L�h $esol�H ��\(-$kdmg\)");
	}


	if($win){
		$ksub2_ex++;
		if($last_battle){
			&K_LOG2("<font color=red>$zname</font>�J��C");
			if($town_get[$zcon] <= 1){
				@NEW_COU=();
				foreach(@COU_DATA){
					($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
					if("$zcon" eq "$xcid"){next;
					}else{
						push(@NEW_COU,"$_");
					}
				}
				open(OUT,">$COUNTRY_LIST") or &ERR('COUNTRY ����g�W�ƾڡC');
				print OUT @NEW_COU;
				close(OUT);
				&MAP_LOG2("<font color=grey>�i���`�j</font>\[$old_date\]$cou_name[$zcon]��a���`�C�C");
				&MAP_LOG("<font color=grey>�i���`�j</font>\[$old_date\]$cou_name[$zcon]��a���`�C�C");
			}
				$zcon = $kcon;
				$znou = int($znou*0.8);
				$zsyo = int($zsyo*0.8);
				$znum = int($znum*0.9);
				$zpri = int($zpri*0.8);
				$kcex += 50;
				$kpos = $cnum;

				&MAP_LOG2("<font color=red>�i��t�j</font>\[$old_date\]$cou_name[$kcon]�ꪺ$kname $zname��t�C");
				&MAP_LOG("<font color=red>�i��t�j</font>\[$old_date\]$cou_name[$kcon]�ꪺ$kname $zname��t�C");
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
			&K_LOG2("$kname $ename���ˡI");
			&E_LOG2("$ename $kname�ѥ_�C�C");
			&MAP_LOG("<font color=red>�i�ӧQ�j</font>$kname $ename���ˡI");
		}
	}else{
		&K_LOG2("$kname $ename�ѥ_�C�C");
		&E_LOG2("$ename $kname���ˡI");
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
#_/       �@LOG �g�J�@       _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub E_LOG2 {

	unshift(@E_LOG2,"$_[0]($mday��$hour��$min��)\n");
}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/       �@LOG �g�J�@       _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub K_LOG2 {

	unshift(@K_LOG2,"$_[0]($mday��$hour��$min��)\n");
}

1;

