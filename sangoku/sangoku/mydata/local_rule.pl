#_/_/_/_/_/_/_/_/_/#
#_/　　國  法　　_/#
#_/_/_/_/_/_/_/_/_/#

sub LOCAL_RULE {

	&CHARA_MAIN_OPEN;

	&COUNTRY_DATA_OPEN("$kcon");
	if($xcid eq "0"){&ERR("無所屬國不能實行。");}
	$sno = $kcex / $LANK;
	if($sno > 20){$sno = 20;}
	$xxins = "<font color=green size=1>$kunit軍 $LANK[$sno] $kname</font>";

	open(IN,"$LOCAL_LIST") or &ERR('沒開文件。err no :country_bbs');
	@LOCAL_DATA = <IN>;
	close(IN);


	&HEADER;

	print <<"EOM";
<div align="center"><TABLE WIDTH="70%" height=100%>
<TBODY><TR>
<TD BGCOLOR=$ELE_BG[$xxele] WIDTH=100% height=5><font color=$ELE_C[$xxele] size=4>＜＜<B> * $xname國法 *</B>＞＞</font></TD>
</TR><TR>
<TD height=5>

<TABLE border="0"><TBODY>
<TR>
<TD></TD>
<TD WIDTH=100% align=center>
<TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>武力</TD><TH>$kstr</TH><TD>知力</TD><TH>$kint</TH><TD>統率力</TD><TH>$klea</TH></TR>
<TR><TD>金</TD><TH>$kgold</TH><TD>米</TD><TH>$krice</TH><TD>貢獻</TD><TH>$kcex</TH></TR>
<TR><TD>所屬國</TD><TH colspan=2>$cou_name[$kcon]國</TH><TD>兵士</TD><TH>$ksol</TH><TD>訓練</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="返回都市"></form>
</TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD height="5">
<div align="center"><TABLE border="0"><TBODY>
<TR><TD bgcolor=$TALK_BG><font color=$TALK_FONT>$xname 預先留下國家的特別規則和重要的信息。<BR>那個國家的參加者$xname只要遵從這個規則行動。<BR>如果有問題請對那個國家的擔當者詢問。(最大20件)</font></TD>
</TR>
</TBODY></TABLE></div>
</TD>
</TR>
<TR>
<TD>
<CENTER>

EOM
	$s_n = 0;
	foreach(@LOCAL_DATA){
		($bbid,$bbno,$bbmes,$bbcharaimg,$bbname,$bbhost,$bbtime,$bbele,$bbcon,$bbtype)=split(/<>/);
		if($kcon eq "$bbcon" && $bbtype eq "0"){
            $mes .= "<TR><TD><input type=radio name=del_id value=$bbno></td><td width=100%><font size=2 color=FFFFFF>$bbmes <font size=1>$bbname</TD></TR>\n";
		$s_n++;
		if($s_n > 15){last;}
		}
	}
print <<"EOM";

<br><form action="$FILE_MYDATA" method="post">
<TABLE border=0 width=80%>
  <TBODY>
    <TR>
      <TD>
      <TABLE border=0 width=100% bgcolor=$ELE_C[$xele]>
        <TBODY bgcolor=$ELE_BG[$xele]>
		$mes
        </TBODY>
      </TABLE>
      </TD>
    </TR>
  </TBODY>
</TABLE><p>

<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=L_RULE_DEL>
<input type=submit value="國法刪除">
</form>

<br><form action="$FILE_MYDATA" method="post">
<textarea name=ins cols=40 rows=4>
</textarea><img src="$IMG/$kchara.gif"><p>

<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=L_RULE_WRITE>
<input type=submit value="國法設定">
</form>
</font>
</CENTER>
</TD>
</TR>
</TBODY></TABLE></div><center>
EOM

	&FOOTER;
	exit;
}
1;