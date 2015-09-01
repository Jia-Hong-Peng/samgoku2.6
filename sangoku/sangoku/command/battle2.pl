#_/_/_/_/_/_/_/_/_/_/#
#¡@ ¡@¡@¾Ôª§¢±¡@ ¡@¡@#
#_/_/_/_/_/_/_/_/_/_/#

sub BATTLE2 {

	if($in{'no'} eq ""){&ERR("NO:¨S¦³¿é¤J¡C");}
	if($in{'num'} eq ""){&ERR("§ð¶iªº«eÀY¨S¦³¿é¤J¡C");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&TIME_DATA;
	$num = $in{'num'};
	$hit=0;

	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
			push(@NEW_COM_DATA,"18<><>$town_name[$num]¥X§L<>$tt<><>$in{'num'}<><>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);

			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"18<><>$town_name[$num]¥X§L<>$tt<><>$in{'num'}<><>\n");
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

	open(OUT,">./charalog/command/$kid.cgi") or &ERR('¥´¤£¶}¤å¥ó¡C');
	print OUT @NEW_COM_DATA;
	close(OUT);

	&HEADER;


	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">NO:$no‚É$town_name[$num]¥X§L¿é¤J¡C</font></h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="½T©w"></form></CENTER><center>
EOM

	&FOOTER;

	exit;

}
1;