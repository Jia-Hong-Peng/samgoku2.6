#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/�@�@�@�@��k�@�d���@�@�@�@_/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub L_RULE_DEL{

	&CHARA_MAIN_OPEN;
	&TIME_DATA;
	&HOST_NAME;
	&COUNTRY_DATA_OPEN("$kcon");

	if($xcid eq "0"){&ERR("�L���ݰꤣ����C");}
	if($in{'del_id'} eq "") { &ERR("�����S����ܡC"); }
	if($kclass < 500){&ERR("��a���^�m���Ȥ�����(500�H�W)");}

	if($lockkey) { &F_LOCK; }
	open(IN,"$LOCAL_LIST") or &ERR2('�S�}���Cerr no :country');
	@LOCAL_DATA = <IN>;
	close(IN);

	$mhit=0;$hit=0;@NEW_LOCAL_DATA=();
	foreach(@LOCAL_DATA){
		($bbid,$bbno,$bbmes,$bbcharaimg,$bbname,$bbhost,$bbtime,$bbele,$bbcon,$bbtype)=split(/<>/);
		if("$bbno" eq "$in{'del_id'}"){
			$hit=1;
			$mes = "$bbmes";
		}else{
			push(@NEW_LOCAL_DATA,"$_");
		}
	}
	if(!$hit){&ERR("���Ӱ�k����R���C");}

	open(OUT,">$LOCAL_LIST") or &ERR('�����}���C');
	print OUT @NEW_LOCAL_DATA;
	close(OUT);

	if (-e $lockfile) { unlink($lockfile); }
	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">$mes�R���C</font></h2><p>

<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=LOCAL_RULE>
<input type=submit value="�T�w"></form></CENTER><center>
EOM
	&FOOTER;
	exit;
	
}
1;