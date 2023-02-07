目录

<a href="#1">1\. 查询指定数据库数据</a>

<a href="#2">2\.统计全部数据</a>

<a href="#3">3\.与正常值差异</a>

---

## <a id="1">1\.查询指定数据库数据</a>
#### 接口功能
> 获取不同类型白血病，不同molecule modules的数据

#### URL
> [https://service-4bv1aeo1-1302618926.bj.apigw.tencentcs.com/release/search]

#### 支持格式
> JSON

#### HTTP请求方式
> GET

#### 请求参数
参数|必选|类型|说明|
-----  |:-------|:-----|-----                               |
data_type    |ture    |string|可选择类型1：lnc；2：Protein-Coding-RNA；3：Alternative-Splicing；    |
cell_type    |true    |string   |可选择类型1：AML；2： APL；3： B-Cell-ALL；4： CLL；5： CML；6： MDS；7： Pre-B-Cell-ALL；8： T-Cell-ALL；9： aCML；|
lnc_id    |false    |string|此项为请求lncRNA数据必填，数据为lncRNA id，举例：NONHSAG058641.2    |
gene_name    |false    |string|此项为请求Protein-Coding-RNA、Alternative-Splicing数据必填，数据为gene名称，举例：ZBP1    |

#### lncRNA数据返回字段
返回字段|字段类型|
-----   |:------
Mean_exp  |float |
id |string |
type |string |
chromosome |string |
start |string |
end |string |
strand |string |

#### 接口示例
> 地址：[https://service-4bv1aeo1-1302618926.bj.apigw.tencentcs.com/release/search?data_type=lnc&cell_type=B-Cell-ALL&id=NONHSAG058641.2]

{"data": [{"Mean_exp": 0.018, "id": "NONHSAG058641.2", "type": "intergenic", "chromosome": "1", "start": "36273", "end": "50392", "strand": "-"}], "total": 1}

#### Protein-Coding-RNA数据返回字段
返回字段|字段类型|
-----   |:------
|Mean_exp  |float |
|id |string |
|gene_name |string |
|chromosome |string |
|start |string |
|end |string |
|strand |string |

#### 接口示例
> 地址：[https://service-4bv1aeo1-1302618926.bj.apigw.tencentcs.com/release/search?data_type=Protein-Coding-RNA&cell_type=B-Cell-ALL&id=ZBP1]

{"data": [{"Mean_exp": 3.0, "id": "ENSG00000124256", "gene_name": "ZBP1", "chromosome": "20", "start": "57603846", "end": "57620576", "strand": "-"}], "total": 1}

#### Alternative-Splicing数据返回字段

##### SE:
返回字段|字段类型|
-----   |:------|
|Type   |string    |
|mean_psi  |float |
|geneSymbol |string |
|geneID |string |
|Chromosome |string |
|strand |string |
|exonStart_0base |string |
|exonEnd |string |
|upstreamEE |string |
|upstreamES |string |
|downstreamEE |string |
|downstreamES |string |

{
    "Type":"SE",
    "mean_psi":3.4,
    "geneSymbol":"ZBP1",
    "geneID":"ENSG00000124256",
    "Chromosome":"chr20",
    "strand":"-",
    "exonStart_0base":"57616243",
    "exonEnd":"57616468",
    "upstreamEE":"57615580",
    "upstreamES":"57615511",
    "downstreamEE":"57620394",
    "downstreamES":"57620261"
}

##### RI:
返回字段|字段类型|
-----   |:------|
|Type   |string    |
|mean_psi  |float |
|geneSymbol |string |
|geneID |string |
|Chromosome |string |
|strand |string |
|riExonStart_0base |string |
|riExonEnd |string |
|upstreamEE |string |
|upstreamES |string |
|downstreamEE |string |
|downstreamES |string |

{
    "Type":"RI",
    "mean_psi":3.4,
    "geneSymbol":"ZBP1",
    "geneID":"ENSG00000124256",
    "Chromosome":"chr20",
    "strand":"-",
    "riExonStart_0base":"57615511",
    "riExonEnd":"57616468",
    "upstreamEE":"57615580",
    "upstreamES":"57615511",
    "downstreamEE":"57616468",
    "downstreamES":"57616243"
}

##### A3SS|A5SS:
返回字段|字段类型|
-----   |:------|
|Type   |string    |
|mean_psi  |float |
|geneSymbol |string |
|geneID |string |
|Chromosome |string |
|strand |string |
|longExonStart_0base |string |
|longExonEnd |string |
|shortEE |string |
|shortES |string |
|flankingEE |string |
|flankingES |string |

{
    "Type":"A3SS",
    "mean_psi":3.6,
    "geneSymbol":"TP53",
    "geneID":"ENSG00000141510",
    "Chromosome":"chr17",
    "strand":"-",
    "longExonStart_0base":"7676520",
    "longExonEnd":"7676622",
    "shortEE":"7676619",
    "shortES":"7676520",
    "flankingEE":"7687487",
    "flankingES":"7687376"
}

##### MXE:
返回字段|字段类型|
-----   |:------|
|Type   |string    |
|mean_psi  |float |
|geneSymbol |string |
|geneID |string |
|Chromosome |string |
|strand |string |
|X1stExonStart_0base |string |
|X1stExonEnd |string |
|X2ndExonStart_0base |string |
|X2ndExonEnd |string |
|upstreamEE |string |
|upstreamES |string |
|downstreamEE |string |
|downstreamES |string |

{
    "Type":"MXE",
    "mean_psi":1.8,
    "geneSymbol":"KDM1A",
    "geneID":"ENSG00000004487",
    "Chromosome":"chr1",
    "strand":"+",
    "X1stExonStart_0base":"23030468",
    "X1stExonEnd":"23030634",
    "X2ndExonStart_0base":"23044426",
    "X2ndExonEnd":"23044486",
    "upstreamEE":"23019947",
    "upstreamES":"23019492",
    "downstreamEE":"23050520",
    "downstreamES":"23050386"
}

#### 接口示例
> 地址：[https://service-4bv1aeo1-1302618926.bj.apigw.tencentcs.com/release/search?data_type=Alternative-Splicing&cell_type=T-Cell-ALL&id=ZBP1]

---
## <a id="2">2\. 统计全部数据</a>
#### 接口功能
> 统计数据库全部数据

#### URL
> [https://service-4bv1aeo1-1302618926.bj.apigw.tencentcs.com/release/total]

#### 支持格式
> JSON

#### HTTP请求方式
> GET

#### 请求参数
> 无

#### 接口示例
> 地址：[https://service-4bv1aeo1-1302618926.bj.apigw.tencentcs.com/release/total]

## <a id="3">3\.与正常值差异(目前仅支持lncRNA)</a>

#### 接口功能
> 查询正常白细胞表达数据平均值与指定类型白血病表达数据平均值差异(目前仅支持lncRNA)

#### URL
> [https://service-4bv1aeo1-1302618926.bj.apigw.tencentcs.com/release/diff]

#### 支持格式
> JSON

#### HTTP请求方式
> GET

#### 请求参数
参数|必选|类型|说明|
-----  |:-------|:-----|-----                               |
cell_type    |true    |list   |可选择类型1：AML；2： APL；3： B-Cell-ALL；4： CLL；5： CML；6： MDS；7： Pre-B-Cell-ALL；8： T-Cell-ALL；9： aCML；请求格式["AML","CML"]|
lnc_id    |false    |string|此项为请求lncRNA数据必填，数据为lncRNA id，举例：NONHSAG058641.2    |

#### lncRNA数据返回字段
返回字段|字段类型|
-----   |:------
Mean_exp  |float |
id |string |
type |string |
chromosome |string |
start |string |
end |string |
strand |string |

#### 接口示例

> 地址：[https://service-4bv1aeo1-1302618926.bj.apigw.tencentcs.com/release/diff?cell_type=["AML","CML"]&lnc_id=NONHSAG058641.2]

{"Normal_white_cell": [{"id": "NONHSAG058641.2", "Mean_exp": 0.0}], "AML": [{"Mean_exp": 0.018, "id": "NONHSAG058641.2", "type": "intergenic", "chromosome": "1", "start": "36273", "end": "50392", "strand": "-"}], "CML": []}
