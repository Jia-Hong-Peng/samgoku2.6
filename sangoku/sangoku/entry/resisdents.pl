#_/_/_/_/_/_/_/_/_/#
#_/　　 說明 　　_/#
#_/_/_/_/_/_/_/_/_/#

sub RESISDENTS {

	&CHARA_MAIN_OPEN;

# 開始遊戲的說明
$P_MES[0] = "歡迎來到三國志.NET的世界！<br>這是一個關於初心者遊戲簡略說明的播放機。";
$P_MES[1] = "首先，遊戲主要都是以實行的指令為主。<BR>最大可輸入２４回合的指令。";
$P_MES[2] = "這個遊戲每３０分鐘時間自動更新。<BR>３０分鐘時間過去的話將前進下一回合。";
$P_MES[3] = "每個回合都會依著武將所輸入的指令實行。<BR>建議你們不要浪費每一個回合，補給指令的輸入。";
$P_MES[4] = "如要執行國家都市的內政指令。<BR>只要在指令選單中選擇所須內政指令便可。";
$P_MES[5] = "農業用地的開發度將影響７月的米收穫，商業開發將影響１月的金收入。<BR>攻擊他國前，強化內攻是必要的。";
$P_MES[6] = "國力富強與人才是統一天下的關鍵要素。<BR>只有國家沒有人才，最終也會被攻破而滅國的。";
$P_MES[7] = "明白了後就立刻開始遊戲吧！";
	&HEADER;

	print <<"EOM";
<div align="center"><TABLE WIDTH="40%" height=100%>
<TBODY><TR>
<TD WIDTH=100% height=5><div align="center"><font color="#FFFFFF" size=4>＜＜<B> * 遊戲的說明 *</B>＞＞</font></div></TD>
</TR><TR>
<TD height=5>
<div align="center"><TABLE border="1" bordercolor="#996600"><TBODY>
<TR>
<TD><img src="$IMG/$kchara.gif"></TD>
<TD>$simg</TD>
<TD>$timg</TD>
<TD bgcolor=$TD_C4 WIDTH=100% align=center></div>
<div align="center"><TABLE bgcolor=$TABLE_C border="0">
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
</TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD height="5">
<TABLE  border="0"><TBODY>
<TR><TD><img src="$IMG/wiz.gif" title="指導員"></TD><TD width="100%" height=100 bgcolor=$TALK_BG><font size=3 color=$TALK_FONT>$P_MES[$in{'num'}]</font></TD>

</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD>
EOM
	$new_num = $in{'num'}+1;
if($new_num < @P_MES){
print "<div align=center><form action=\"$FILE_ENTRY\" method=\"post\">
<input type=hidden name=id value=$kid>
<input type=hidden name=num value=$new_num>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=RESISDENTS>
<input type=submit value=\"次頁\"></form>";
}
print<<"EOM";
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="開始遊戲"></form></div>

</TD>
</TR>
</TBODY></TABLE></div><center>
EOM

	&FOOTER;
	exit;
}
1;