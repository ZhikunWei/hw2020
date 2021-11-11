Project1 数据文件

提供的数据包括
1. en_instance_list.txt和fr_instance_list.txt，英语和法语的instance列表，提供每个instance的label。
2. class_list.txt，class列表，提供每个class的label。
3. property_list.txt，property列表，提供每个属性的label。
4. CL_link.txt，instance之间的sameAs关系，即跨语言链接，格式为：en instance label  \t\t  fr insatnce label。
5. subClassOf.txt，class之间的subclassof关系，格式为：class label  \t\t  super-class label。
6. domain.txt，property的domain，格式为：property label \t\t  class label。
7. range.txt，property的range，格式为：property label \t\t  class label 或者 property label \t\t  datatype。
说明：range如果是一个class，一般表示对象型属性，range如果是某个datatype，一般表示数值型属性，因为使用RDF模型，在这里不做区分，
datatype的定义会提供代码。
8. instanceOf.txt，英语和法语中的instanceof关系，格式为：instance label \t\t  class label。
9. en_object_triples.txt和fr_object_triples.txt，英语和法语中，instance的对象型属性三元组，
格式为：instance label  \t\t  property label  \t\t  instance label。
10. en_datatype_triples.txt和fr_datatype_triples.txt，英语和法语中，instance的数值型属性三元组，
格式为：instance label  \t\t  property label  \t\t  property-value。


所有文件每一行中的分隔符都是\t\t（如果有的话），schema定义部分提供了样例代码。

说明：在DBpedia中，理论上不同语言使用同样的schema，即不同语言下，使用同样的class和property，
一套通用的class和property被所有语言共享，只有instance是不同的。
