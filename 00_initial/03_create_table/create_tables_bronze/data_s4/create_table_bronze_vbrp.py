# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists bronze.vbrp ;
# MAGIC create table bronze.vbrp
# MAGIC 
# MAGIC (MANDT string,
# MAGIC  VBELN string,
# MAGIC  POSNR string,
# MAGIC  UEPOS string,
# MAGIC  FKIMG string,
# MAGIC  VRKME string,
# MAGIC  UMVKZ string,
# MAGIC  UMVKN string,
# MAGIC  MEINS string,
# MAGIC  SMENG string,
# MAGIC  FKLMG string,
# MAGIC  LMENG string,
# MAGIC  NTGEW string,
# MAGIC  BRGEW string,
# MAGIC  GEWEI string,
# MAGIC  VOLUM string,
# MAGIC  VOLEH string,
# MAGIC  GSBER string,
# MAGIC  PRSDT string,
# MAGIC  FBUDA string,
# MAGIC  KURSK string,
# MAGIC  NETWR string,
# MAGIC  VBELV string,
# MAGIC  POSNV string,
# MAGIC  VGBEL string,
# MAGIC  VGPOS string,
# MAGIC  VGTYP string,
# MAGIC  AUBEL string,
# MAGIC  AUPOS string,
# MAGIC  AUREF string,
# MAGIC  MATNR string,
# MAGIC  ARKTX string,
# MAGIC  PMATN string,
# MAGIC  CHARG string,
# MAGIC  MATKL string,
# MAGIC  PSTYV string,
# MAGIC  POSAR string,
# MAGIC  PRODH string,
# MAGIC  VSTEL string,
# MAGIC  ATPKZ string,
# MAGIC  SPART string,
# MAGIC  POSPA string,
# MAGIC  WERKS string,
# MAGIC  ALAND string,
# MAGIC  WKREG string,
# MAGIC  WKCOU string,
# MAGIC  WKCTY string,
# MAGIC  TAXM1 string,
# MAGIC  TAXM2 string,
# MAGIC  TAXM3 string,
# MAGIC  TAXM4 string,
# MAGIC  TAXM5 string,
# MAGIC  TAXM6 string,
# MAGIC  TAXM7 string,
# MAGIC  TAXM8 string,
# MAGIC  TAXM9 string,
# MAGIC  KOWRR string,
# MAGIC  PRSFD string,
# MAGIC  SKTOF string,
# MAGIC  SKFBP string,
# MAGIC  KONDM string,
# MAGIC  KTGRM string,
# MAGIC  KOSTL string,
# MAGIC  BONUS string,
# MAGIC  PROVG string,
# MAGIC  EANNR string,
# MAGIC  VKGRP string,
# MAGIC  VKBUR string,
# MAGIC  SPARA string,
# MAGIC  SHKZG string,
# MAGIC  ERNAM string,
# MAGIC  ERDAT string,
# MAGIC  ERZET string,
# MAGIC  BWTAR string,
# MAGIC  LGORT string,
# MAGIC  STAFO string,
# MAGIC  WAVWR string,
# MAGIC  KZWI1 string,
# MAGIC  KZWI2 string,
# MAGIC  KZWI3 string,
# MAGIC  KZWI4 string,
# MAGIC  KZWI5 string,
# MAGIC  KZWI6 string,
# MAGIC  STCUR string,
# MAGIC  UVPRS string,
# MAGIC  UVALL string,
# MAGIC  EAN11 string,
# MAGIC  PRCTR string,
# MAGIC  KVGR1 string,
# MAGIC  KVGR2 string,
# MAGIC  KVGR3 string,
# MAGIC  KVGR4 string,
# MAGIC  KVGR5 string,
# MAGIC  MVGR1 string,
# MAGIC  MVGR2 string,
# MAGIC  MVGR3 string,
# MAGIC  MVGR4 string,
# MAGIC  MVGR5 string,
# MAGIC  MATWA string,
# MAGIC  BONBA string,
# MAGIC  KOKRS string,
# MAGIC  PAOBJNR string,
# MAGIC  PS_PSP_PNR string,
# MAGIC  AUFNR string,
# MAGIC  TXJCD string,
# MAGIC  CMPRE string,
# MAGIC  CMPNT string,
# MAGIC  CUOBJ string,
# MAGIC  CUOBJ_CH string,
# MAGIC  KOUPD string,
# MAGIC  UECHA string,
# MAGIC  XCHAR string,
# MAGIC  ABRVW string,
# MAGIC  SERNR string,
# MAGIC  BZIRK_AUFT string,
# MAGIC  KDGRP_AUFT string,
# MAGIC  KONDA_AUFT string,
# MAGIC  LLAND_AUFT string,
# MAGIC  MPROK string,
# MAGIC  PLTYP_AUFT string,
# MAGIC  REGIO_AUFT string,
# MAGIC  VKORG_AUFT string,
# MAGIC  VTWEG_AUFT string,
# MAGIC  ABRBG string,
# MAGIC  PROSA string,
# MAGIC  UEPVW string,
# MAGIC  AUTYP string,
# MAGIC  STADAT string,
# MAGIC  FPLNR string,
# MAGIC  FPLTR string,
# MAGIC  AKTNR string,
# MAGIC  KNUMA_PI string,
# MAGIC  KNUMA_AG string,
# MAGIC  MWSBP string,
# MAGIC  AUGRU_AUFT string,
# MAGIC  FAREG string,
# MAGIC  UPMAT string,
# MAGIC  UKONM string,
# MAGIC  CMPRE_FLT string,
# MAGIC  ABFOR string,
# MAGIC  ABGES string,
# MAGIC  J_1ARFZ string,
# MAGIC  J_1AREGIO string,
# MAGIC  J_1AGICD string,
# MAGIC  J_1ADTYP string,
# MAGIC  J_1ATXREL string,
# MAGIC  J_1BCFOP string,
# MAGIC  J_1BTAXLW1 string,
# MAGIC  J_1BTAXLW2 string,
# MAGIC  J_1BTXSDC string,
# MAGIC  BRTWR string,
# MAGIC  WKTNR string,
# MAGIC  WKTPS string,
# MAGIC  RPLNR string,
# MAGIC  KURSK_DAT string,
# MAGIC  WGRU1 string,
# MAGIC  WGRU2 string,
# MAGIC  KDKG1 string,
# MAGIC  KDKG2 string,
# MAGIC  KDKG3 string,
# MAGIC  KDKG4 string,
# MAGIC  KDKG5 string,
# MAGIC  VKAUS string,
# MAGIC  J_1AINDXP string,
# MAGIC  J_1AIDATEP string,
# MAGIC  KZFME string,
# MAGIC  MWSKZ string,
# MAGIC  VERTT string,
# MAGIC  VERTN string,
# MAGIC  SGTXT string,
# MAGIC  DELCO string,
# MAGIC  BEMOT string,
# MAGIC  RRREL string,
# MAGIC  WMINR string,
# MAGIC  VGBEL_EX string,
# MAGIC  VGPOS_EX string,
# MAGIC  LOGSYS string,
# MAGIC  VGTYP_EX string,
# MAGIC  J_1BTAXLW3 string,
# MAGIC  J_1BTAXLW4 string,
# MAGIC  J_1BTAXLW5 string,
# MAGIC  MSR_ID string,
# MAGIC  MSR_REFUND_CODE string,
# MAGIC  MSR_RET_REASON string,
# MAGIC  NRAB_KNUMH string,
# MAGIC  NRAB_VALUE string,
# MAGIC  DISPUTE_CASE string,
# MAGIC  FUND_USAGE_ITEM string,
# MAGIC  FARR_RELTYPE string,
# MAGIC  CLAIMS_TAXATION string,
# MAGIC  KURRF_DAT_ORIG string,
# MAGIC  SGT_RCAT string,
# MAGIC  SGT_SCAT string,
# MAGIC  PREFE string,
# MAGIC  AKKUR string,
# MAGIC  WAERK string,
# MAGIC  DRAFT string,
# MAGIC  ACTIVEDOCUMENT string,
# MAGIC  GRWRT string,
# MAGIC  FKSAA string,
# MAGIC  ABSTA string,
# MAGIC  ABGRU string,
# MAGIC  MWSK1 string,
# MAGIC  DATAAGING string,
# MAGIC  DUMMY_BILLGDOCITEM_INCL_EEW_PS string,
# MAGIC  ZZ1_PLATAFORMA_BDI string,
# MAGIC  ZZ1_CATEGORIA_BDI string,
# MAGIC  ZZ1_TERRENO_BDI string,
# MAGIC  ZZ1_VARIEDAD_BDI string,
# MAGIC  ZZ1_PRESENTACION_BDI string,
# MAGIC  ZZ1_SUB_PLATAFORMA_BDI string,
# MAGIC  ZZ1_FAMILIA_BDI string,
# MAGIC  ZZ1_TERRITORIO_BDI string,
# MAGIC  CWM_MENGE string,
# MAGIC  CWM_MEINS string,
# MAGIC  ZAPCGKI string,
# MAGIC  APCGK_EXTENDI string,
# MAGIC  ZABDATI string,
# MAGIC  AUFPL string,
# MAGIC  APLZL string,
# MAGIC  DPCNR string,
# MAGIC  DCPNR string,
# MAGIC  DPNRB string,
# MAGIC  BOSFAR string,
# MAGIC  DP_BELNR string,
# MAGIC  DP_BUKRS string,
# MAGIC  DP_GJAHR string,
# MAGIC  DP_BUZEI string,
# MAGIC  PACKNO string,
# MAGIC  PEROP_BEG string,
# MAGIC  PEROP_END string,
# MAGIC  FMFGUS_KEY string,
# MAGIC  FSH_SEASON_YEAR string,
# MAGIC  FSH_SEASON string,
# MAGIC  FSH_COLLECTION string,
# MAGIC  FSH_THEME string,
# MAGIC  FONDS string,
# MAGIC  FISTL string,
# MAGIC  FKBER string,
# MAGIC  GRANT_NBR string,
# MAGIC  BUDGET_PD string,
# MAGIC  J_3GBELNRI string,
# MAGIC  J_3GPMAUFE string,
# MAGIC  J_3GPMAUFV string,
# MAGIC  J_3GETYPA string,
# MAGIC  J_3GETYPE string,
# MAGIC  J_3GORGUEB string,
# MAGIC  PRS_WORK_PERIOD string,
# MAGIC  PPRCTR string,
# MAGIC  PARGB string,
# MAGIC  AUFPL_OAA string,
# MAGIC  APLZL_OAA string,
# MAGIC  CAMPAIGN string,
# MAGIC  COMPREAS string,
# MAGIC  WRF_CHARSTC1 string,
# MAGIC  WRF_CHARSTC2 string,
# MAGIC  WRF_CHARSTC3 string,
# MAGIC  ZZTIPO_IMP string,
# MAGIC  ZZKUNG string,
# MAGIC 
# MAGIC CREATE_AT timestamp,
# MAGIC YEAR_MONTH_DAY string,
# MAGIC ORIGIN_FILE string
# MAGIC )
# MAGIC using delta
# MAGIC partitioned by (YEAR_MONTH_DAY)
# MAGIC LOCATION '/mnt/data_s4/bronze/vbrp'