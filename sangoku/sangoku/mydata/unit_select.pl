#_/_/_/_/_/_/_/_/_/#
#_/ 　部隊配屬　 _/#
#_/_/_/_/_/_/_/_/_/#

sub UNIT_SELECT {

	&CHARA_MAIN_OPEN;

	open(IN,"$TOWN_LIST") or &ERR("打不開指定的文件。");
	@TOWN_DATA = <IN>;
	close(IN);
	foreach(@TOWN_DATA){
		($zcid,$zname,$zele,$zcon,$zmoney,$zmes)=split(/<>/);
		if("$zcid" eq "$in{town}"){last;}
	}


	open(IN,"$UNIT_LIST") or &ERR("打不開指定的文件。");
	@UNI_DATA = <IN>;
	close(IN);

	@UNI_DATA2 = @UNI_DATA;
	$i=0;
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if("$ucon" eq "$kcon" && $ureader){

			$unit_num=1;
			$unit_list = "$uname";

			if($uid eq $kid){
				foreach(@UNI_DATA2){
					($unit_id2,$uunit_name2,$ucon2,$ureader2,$uid2,$uname2,$uchara2,$umes2,$uflg2)=split(/<>/);
					if("$unit_id" eq "$unit_id2" && !$ureader2){
						$unit_list .= ",$uname2";
						$unit_num++;
						$u_member .= "<option value=$uid2>$uname2";
					}
				}

			}else{
				foreach(@UNI_DATA2){
					($unit_id2,$uunit_name2,$ucon2,$ureader2,$uid2,$uname2,$uchara2,$umes2,$uflg2)=split(/<>/);
					if("$unit_id" eq "$unit_id2" && !$ureader2){
						$unit_list .= ",$uname2";
						$unit_num++;
					}
				}
			}
			if($uflg eq "1"){
				$u_mes = "入隊拒絕";
			}else{
				$u_mes = "入隊\許\可";
			}
			$unit_party .= "<TR><TD bgcolor=$TD_C3><input type=radio name=unit_id value=$unit_id></TD><TD bgcolor=$TD_C2><img src=\"$IMG/$uchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$uname\"></TD><TD bgcolor=$TD_C1><font size=1>$uunit_name部隊<BR>($uname)</TD><td bgcolor=$TD_C1>$unit_list</td><td bgcolor=$TD_C2>$unit_num人</td><td bgcolor=$TD_C2>$umes</td><TD bgcolor=$TD_C1>$u_mes</TD></tr>";
		}

		if($uid eq $kid){
			$k_hit=1;
			$kunit_name = $uunit_name;
		}
	}

	if(!$k_hit){
		$kunit_name = "無所屬";
	}

	&HEADER;

	print <<"EOM";
<div align="center"><table width="70%" cellpadding="0" cellspacing="0" border=0><tr><td>
<TABLE WIDTH="100%" border=0>
<TBODY><TR>
<TD BGCOLOR=$ELE_BG[$kele] WIDTH=100% height=5><div align="center"><font color=$ELE_C[$kele] size=4>＜＜<B> * 部 隊 分 配．編 成*</B>＞＞</font></div></TD>
</TR><TR>
<TD bgcolor=$TD_C4 height=5>
<TABLE border="0"><TBODY>
<TR>
<TD bgcolor=$TD_C1><img src="$IMG/$kchara.gif" width="$img_wid" height="$img_height" alt="$kname"></TD>
<TD bgcolor=$TD_C2>$simg</TD>
<TD bgcolor=$TD_C3>$timg</TD>
<TD bgcolor=$TD_C4 WIDTH=100% align=center>
<table cellpadding="0" cellspacing="0" border=0><tr><td bgcolor=$TABLE_C>
<TABLE border="0" cellspacing="2">
<TBODY>
<TR>
<TD bgcolor=$TD_C2>名字</TD>
<TD bgcolor=$TD_C3>等級</TD>
<TD bgcolor=$TD_C2>屬性</TD>
<TD bgcolor=$TD_C3>職業</TD>
</TR>
<TR>
<TD bgcolor=$TD_C2>$kname</TD>
<TD bgcolor=$TD_C3 align=right>$klv</TD>
<TD bgcolor=$TD_C2>$ELE[$kele]屬</TD>
<TD bgcolor=$TD_C3>$SYOKU[$kclass]</TD>
</TR>
<TR>
<TD bgcolor=$TD_C2>所持金</TD>
<TD bgcolor=$TD_C1 colspan=3 align=right>$kgold GOLD</TD>
</TR>
</TBODY></TABLE>
</td></tr></table>
</TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD height="5">
<TABLE  border="0"><TBODY>
<TR><TD width="100%" bgcolor=$TALK_BG><font color=$TALK_FONT>這裡能編成屬於本國的部隊。<BR>你現在從屬<font color=red>$kunit_name</font>部隊。<BR>可使用部隊跟所屬部隊的聊天和指令。</font></TD>
<TD bgcolor=$TD_C4></TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD><BR><BR>
<form action="$FILE_MYDATA" method="post">
<CENTER><TABLE bgcolor=$TABLE_C><TBODY><TR>
<TD bgcolor=$TD_C3>選擇</TD><TD bgcolor=$TD_C2>隊長</TD><TD bgcolor=$TD_C1>部隊名(隊長)</TD><TD bgcolor=$TD_C1>配屬部隊</TD><TD bgcolor=$TD_C1>部隊數</TD><TD bgcolor=$TD_C2>部隊募集消息</TD><TD bgcolor=$TD_C1>入隊接待</TD></TR>
EOM


print <<"EOM";
$unit_party
</TR></TBODY></TABLE></CENTER>

<BR>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=UNIT_ENTRY>
<input type=submit value="從屬"></form>
<HR size=0>
<h3><font color=3355AA><b>部隊長指令</B></font></h3>

<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=UNIT_CHANGE>
<input type=submit value="入隊拒絕．\許\可"></form>
※實行後不能加入其他部隊。<p>

<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<select name=did>$u_member</select>
<input type=hidden name=mode value=UNIT_OUT>
<input type=submit value="成員解雇"></form>
※實行後那個成員便會脫離部隊。<p>


<HR size=0>

<b class=\"clit\">新規部隊作成</B></font> (階級價值500以上必要)
<form action="$FILE_MYDATA" method="post">
<TABLE bgcolor=$TABLE_C><TR><TD bgcolor=$TD_C3>部隊名</TD><TD bgcolor=$TD_C2><input type=text name=name size=30><BR>[全角大字2～8個字以內]</TD></TR>
<TD bgcolor=$TD_C3>部隊募集宣傳語</TD><TD bgcolor=$TD_C2><input type=text name=mes size=30><BR>[全角大字0～20個字以內]</TD>
</TABLE>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=MAKE_UNIT>
<input type=submit value="部隊作成"></form>
<HR size=0>
<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=UNIT_DELETE>
<input type=submit value="部隊脫離．解散"></form>
<HR size=0>


<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="返回都市"></form>
</TD>
</TR>
</TBODY></TABLE>
</td></tr></table></div><center>
EOM

	&FOOTER;
	exit;
}
1;