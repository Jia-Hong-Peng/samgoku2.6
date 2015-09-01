#_/_/_/_/_/_/_/_/_/_/_/#
#_/¡@¡@F MAP µe­±¡@¡@_/#
#_/_/_/_/_/_/_/_/_/_/_/#

sub OPEN_MAP {


	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);

	$p=0;
	while($p<15){
		$S_MES .= "¡D$S_MOVE[$p]<BR>";
		$p++;
	}

	open(IN,"$MAP_LOG_LIST2");
	@S_MOVE = <IN>;
	close(IN);

	$p=0;
	while($p<20){
		$D_MES .= "¡D$S_MOVE[$p]<BR>";
		$p++;
	}

	&TIME_DATA;
	if($hour < 6){$time_img = 2;$table_font = "#FFFFFF";$table_color = "#000000";
	}elsif($hour > 18){$time_img = 2;$table_font = "#FFFFFF";$table_color = "#000000";
	}elsif($hour > 15){$time_img = 2;$table_font = "#FFFFFF";$table_color = "#804020";
	}elsif($hour > 12){$time_img = 1;$table_font = "#000000";$table_color = "#FFFFDC";
	}else{$time_img = 0;$table_font = "#000000";$table_color = "#FFEFCC";}

	open(IN,"$COUNTRY_LIST") or &ERR2('¨S¶}¤å¥ó¡Cerr no :country');
	@COU_DATA = <IN>;
	close(IN);
	foreach(@COU_DATA){
		($x2cid,$x2name,$x2ele,$x2mark)=split(/<>/);
		$cou_name[$x2cid] = "$x2name";
		$cou_ele[$x2cid] = "$x2ele";
		$cou_mark[$x2cid] = "$x2mark";
	}


	$data_mes .= "<TR><Th colspan=3 bgcolor=$TD_C2>¦U°ê¼Æ¾Ú</Th></tr><TR><Th bgcolor=$TD_C4>°ê®aµn¿ýªÌ</Th><Th bgcolor=$TD_C4>¸êª÷</Th><Th bgcolor=$TD_C4>­n¶ë­@¤[¤O</Th></TR>";
	$country_no=0;$i=1;
	foreach(@COU_DATA){
		($xxcid,$xxname,$xxele,$xxnum,$xxins,$xxind,$xxall,$xxgold,$xxhp,$xxmaxhp,$xxstr,$xxvit,$xxagi)=split(/<>/);
		if($all_gold){
		$n_gold = int(($xxgold/($all_gold))*1000)/10;
		}else{
		$n_gold = 0;
		}
		if($all_num){
		$n_num  = int(($xxnum/($all_num))*1000)/10;
		}else{
		$n_num  = 0;
		}
		$data_mes .= "<TR><Th bgcolor=$ELE_BG[$xxele] colspan=3><font color=$ELE_C[$xxele]>$xxname °ê</Th></TR><TR><Th bgcolor=$TD_C4>$xxnum¦W($n_num\%)</Th><Th bgcolor=$TD_C4>$xxgold Gold($n_gold\%)</Th><Th bgcolor=$TD_C4>$xxhp/$xxmaxhp</Th></TR>";
		$c_gold[$i] = $xxgold;
		$c_num[$i] = $xxnum;
		$i++;
	}

	$zmes="";

	&HEADER;
print <<"EOM";
<div align="center"><TABLE bgcolor=$TABLE_C width=70% border="0">
  <TBODY>
    <TR>
      <TD bgcolor=$table_color width=40%>
      <TABLE width=80% border="0">
        <TBODY>
          <TR>
            <TH><font color=$table_font><font size=4>$GAME_TITLE</font> <BR>- ¤j ³° ¦a ¹Ï -</font></TH>
          </TR>
        </TBODY>
      </TABLE>
      <TABLE bgcolor=$TD_C2 background="$IMG/mapbg.gif" width=100% height=5 border="0">
        <TBODY>
          <TR>
            <TD width=20 bgcolor=$TD_C2>-</TD>
EOM
	open(IN,"$TOWN_LIST") or &ERR("¥´¤£¶}«ü©wªº¤å¥ó¡C");
	@TOWN_DATA = <IN>;
	close(IN);

    for($i=1;$i<11;$i++){
		print "<TD width=20 bgcolor=$TD_C1>$i</TD>";
	}
	print "</TR>";
     for($i=0;$i<10;$i++){
		$n = $i+1;
		print "<TR><TD bgcolor=$TD_C3>$n</td>";
		for($j=0;$j<10;$j++){
				$m_hit=0;
				foreach(@TOWN_DATA){
					($zzname,$zzcon,$zznum,$zznou,$zzsyo,$zzshiro,$zznou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy)=split(/<>/);
					if("$zzx" eq "$j" && "$zzy" eq "$i"){$m_hit=1;last;}
				}
				if($m_hit){
					if($zzname eq "¬¥¶§" || $zzname eq "«Ø·~" || $zzname eq "¦¨³£" || $zzname eq "·~" ){
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><img src=$IMG/m_1.gif width=16 height=16 border=0 alt=$zznamey$cou_name[$zzcon]z></TH>";
					}else{
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><img src=$IMG/m_4.gif width=16 height=16 border=0 alt=$zznamey$cou_name[$zzcon]z></TH>";
					}
				}else{
					print "<TH>&nbsp;</TH>";
				}
		}
		print "</TR>";
	}

print <<"EOM";
        </TBODY>
      </TABLE>
      </TD>
      <TD bgcolor=$TD_C3>
      <TABLE width=100% border="0">
        <TBODY>
          <TR>
            <TH bgcolor=$TD_C4>MAP LOG</TH></TR><TR>
<TD bgcolor=$TD_1>$S_MES</TD>
          </TR>
        </TBODY>
      </TABLE>
</TD>
    </TR>
<TR>      <TD colspan=2 bgcolor=$TD_C3>
      <TABLE width=100% border="0">
        <TBODY>
          <TR>
            <TH bgcolor=$TD_C4>¥v°O</TH></TR><TR>
<TD bgcolor=$TD_1>$D_MES</TD>
          </TR>
        </TBODY>
      </TABLE>
</TD>
    </TR>
  </TBODY>
</TABLE></div><br>
<table width="70%" border="0" align="center" cellspacing="0">
    <tr>
      <td><font color=#FFFFFF>¡°µó¦Wªí¥Ü¡C</font><br>
<font color=#FFFFFF>$daytime</font></td>
    </tr>
  </table><center>
EOM
	&FOOTER;
	exit;

}
1;