chars = '''
अ	आ	इ	ई	उ	ऊ	ए	ऐ	ओ	औ	अं	अः
क	का	कि	की	कु	कू	के	कै	को	कौ	कं	कः
ख	खा	खि	खी	खु	खू	खे	खै	खो	खौ	खं	खः
ग	गा	गि	गी	गु	गू	गे	गै	गो	गौ	गं	गः
घ	घा	घि	घी	घु	घू	घे	घै	घो	घौ	घं	घः
ङ	ङा	ङि	ङी	ङु	ङू	ङे	ङै	ङो	ङौ	ङं	ङः
च	चा	चि	ची	चु	चू	चे	चै	चो	चौ	चं	चः
छ	छा	छि	छी	छु	छू	छे	छै	छो	छौ	छं	छः
ज	जा	जि	जी	जु	जू	जे	जै	जो	जौ	जं	जः
झ	झा	झि	झी	झु	झू	झे	झै	झो	झौ	झं	झः
ञ	ञा	ञि	ञी	ञु	ञू	ञे	ञै	ञो	ञौ	ञं	ञः
ट	टा	टि	टी	टु	टू	टे	टै	टो	टौ	टं	टः
ठ	ठा	ठि	ठी	ठु	ठू	ठे	ठै	ठो	ठौ	ठं	ठः
ड	डा	डि	डी	डु	डू	डे	डै	डो	डौ	डं	डः
ढ	ढा	ढि	ढी	ढु	ढू	ढे	ढै	ढो	ढौ	ढं	ढः
ण	णा	णि	णी	णु	णू	णे	णै	णो	णौ	णं	णः
त	ता	ति	ती	तु	तू	ते	तै	तो	तौ	तं	तः
थ	था	थि	थी	थु	थू	थे	थै	थो	थौ	थं	थः
द	दा	दि	दी	दु	दू	दे	दै	दो	दौ	दं	दः
ध	धा	धि	धी	धु	धू	धे	धै	धो	धौ	धं	धः
न	ना	नि	नी	नु	नू	ने	नै	नो	नौ	नं	नः
प	पा	पि	पी	पु	पू	पे	पै	पो	पौ	पं	पः
फ	फा	फि	फी	फु	फू	फे	फै	फो	फौ	फं	फः
ब	बा	बि	बी	बु	बू	बे	बै	बो	बौ	बं	बः
भ	भा	भि	भी	भु	भू	भे	भै	भो	भौ	भं	भः
म	मा	मि	मी	मु	मू	मे	मै	मो	मौ	मं	मः
य	या	यि	यी	यु	यू	ये	यै	यो	यौ	यं	यः
र	रा	रि	री	रु	रू	रे	रै	रो	रौ	रं	रः
ल	ला	लि	ली	लु	लू	ले	लै	लो	लौ	लं	लः
व	वा	वि	वी	वु	वू	वे	वै	वो	वौ	वं	वः
श	शा	शि	शी	शु	शू	शे	शै	शो	शौ	शं	शः
ष	षा	षि	षी	षु	षू	षे	षै	षो	षौ	षं	षः
स	सा	सि	सी	सु	सू	से	सै	सो	सौ	सं	सः
ह	हा	हि	ही	हु	हू	हे	है	हो	हौ	हं	हः
'''

'''
[]
'''


'''
"अ","आ","इ","ई","उ","ऊ","ए","ऐ","ओ","औ","अ","अ","क","क","ा","क","ि","क","ी","क","ु","क","ू","क","े","क","ै","क","ो","क","ौ","क","क","ख","ख","ा","ख","ि","ख","ी","ख","ु","ख","ू","ख","े","ख","ै","ख","ो","ख","ौ","ख","ख","         ,"ग","ग","ा","ग","ि","ग","ी","ग","ु","ग","ू","ग","े","ग","ै","ग","ो","ग","ौ","ग","ग","घ","घ","ा","घ","ि","घ","ी","घ","ु","घ","ू","घ","े","घ","ै","घ","ो","घ","ौ","घ","घ","ङ","ङ","ा","ङ","ि","ङ","ी","ङ","ु","ङ","ू","ङ","े           े","ङ","ै","ङ","ो","ङ","ौ","ङ","ङ","च","च","ा","च","ि","च","ी","च","ु","च","ू","च","े","च","ै","च","ो","च","ौ","च","च","छ","छ","ा","छ","ि","छ","ी","छ","ु","छ","ू","छ","े","छ","ै","छ","ो","छ","ौ","छ","छ","ज","ज","ा"            ","ज","ि","ज","ी","ज","ु","ज","ू","ज","े","ज","ै","ज","ो","ज","ौ","ज","ज","झ","झ","ा","झ","ि","झ","ी","झ","ु","झ","ू","झ","े","झ","ै","झ","ो","झ","ौ","झ","झ","ञ","ञ","ा","ञ","ि","ञ","ी","ञ","ु","ञ","ू","ञ","े","ञ","ै","ञ",             ,"ो","ञ","ौ","ञ","ञ","ट","ट","ा","ट","ि","ट","ी","ट","ु","ट","ू","ट","े","ट","ै","ट","ो","ट","ौ","ट","ट","ठ","ठ","ा","ठ","ि","ठ","ी","ठ","ु","ठ","ू","ठ","े","ठ","ै","ठ","ो","ठ","ौ","ठ","ठ","ड","ड","ा","ड","ि","ड","          "ी","ड","ु","ड","ू","ड","े","ड","ै","ड","ो","ड","ौ","ड","ड","ढ","ढ","ा","ढ","ि","ढ","ी","ढ","ु","ढ","ू","ढ","े","ढ","ै","ढ","ो","ढ","ौ","ढ","ढ","ण","ण","ा","ण","ि","ण","ी","ण","ु","ण","ू","ण","े","ण","ै","ण","ो","ण","ौ","ण             ण","ण","त","त","ा","त","ि","त","ी","त","ु","त","ू","त","े","त","ै","त","ो","त","ौ","त","त","थ","थ","ा","थ","ि","थ","ी","थ","ु","थ","ू","थ","े","थ","ै","थ","ो","थ","ौ","थ","थ","द","द","ा","द","ि","द","ी","द","ु","द"           ","ू","द","े","द","ै","द","ो","द","ौ","द","द","ध","ध","ा","ध","ि","ध","ी","ध","ु","ध","ू","ध","े","ध","ै","ध","ो","ध","ौ","ध","ध","न","न","ा","न","ि","न","ी","न","ु","न","ू","न","े","न","ै","न","ो","न","ौ","न","न",             ,"प","प","ा","प","ि","प","ी","प","ु","प","ू","प","े","प","ै","प","ो","प","ौ","प","प","फ","फ","ा","फ","ि","फ","ी","फ","ु","फ","ू","फ","े","फ","ै","फ","ो","फ","ौ","फ","फ","ब","ब","ा","ब","ि","ब","ी","ब","ु","ब","ू","ब","े","            "ब","ै","ब","ो","ब","ौ","ब","ब","भ","भ","ा","भ","ि","भ","ी","भ","ु","भ","ू","भ","े","भ","ै","भ","ो","भ","ौ","भ","भ","म","म","ा","म","ि","म","ी","म","ु","म","ू","म","े","म","ै","म","ो","म","ौ","म","म","य","य","ा","य           य","ि","य","ी","य","ु","य","ू","य","े","य","ै","य","ो","य","ौ","य","य","र","र","ा","र","ि","र","ी","र","ु","र","ू","र","े","र","ै","र","ो","र","ौ","र","र","ल","ल","ा","ल","ि","ल","ी","ल","ु","ल","ू","ल","े","ल","ै","ल","ो"             ","ल","ौ","ल","ल","व","व","ा","व","ि","व","ी","व","ु","व","ू","व","े","व","ै","व","ो","व","ौ","व","व","श","श","ा","श","ि","श","ी","श","ु","श","ू","श","े","श","ै","श","ो","श","ौ","श","श","ष","ष","ा","ष","ि","ष","ी",          ,"ष","ु","ष","ू","ष","े","ष","ै","ष","ो","ष","ौ","ष","ष","स","स","ा","स","ि","स","ी","स","ु","स","ू","स","े","स","ै","स","ो","स","ौ","स","स","ह","ह","ा","ह","ि","ह","ी","ह","ु","ह","ू","ह","े","ह","ै","ह","ो","ह","ौ","ह","             "ह"
'''

chars_new = ''''
अ,आ,इ,ई,उ,ऊ,ए,ऐ,ओ,औ,अं,अः,क,का,कि,की,कु,कू,के,कै,को,कौ,कं,कः,ख,खा,खि,खी,खु,खू,खे,खै,खो,खौ,खं,खः,ग,गा,गि,गी,गु,गू,गे,गै,गो,गौ,गं,गः,घ,घा,घि,घी,घु,घू,घे,घै,घो,घौ,घं,घः,ङ,ङा,ङि,ङी,ङु,ङू,ङे,ङै,ङो,ङौ,ङं,ङः,च,चा,चि,ची,चु,चू,चे,चै,चो,चौ,चं,चः,,छ,छा,छि,छी,छु,छू,छे,छै,छो,छौ,छं,छः,ज,जा,जि,जी,जु,जू,जे,जै,जो,जौ,जं,जः,झ,झा,झि,झी,झु,झू,झे,झै,झो,झौ,झं,झः,ञ,ञा,ञि,ञी,ञु,ञू,ञे,ञै,ञो,ञौ,ञं,ञः,ट,टा,टि,टी,टु,टू,टे,टै,टो,टौ,टं,टः,ठ,ठा,ठि,ठी,ठु,ठू,ठे,ठै,ठो,ठौ,ठं,ठः,ड,डा,डि,डी,डु,डू,डे,डै,डो,ड,डौ,डं,डः,ढ,ढा,ढि,ढी,ढु,ढू,ढे,ढै,ढो,ढौ,ढं,ढः,ण,णा,णि,णी,णु,णू,णे,णै,णो,णौ,णं,णः,त,ता,ति,ती,तु,तू,ते,तै,तो,तौ,तं,तः,थ,था,थि,थी,थु,थू,थे,थै,थो,थौ,थं,थः,द,दा,दि,दी,दु,दू,दे,दै,दो,दौ,दं,दः,ध,धा,धि,धी,धु,धू,धे,धै,धो,धौ,धं,धः,न,ना,नि,नी,नु,नू,ने,नै,नो,नौ,नं,नः,प,पा,पि,पी,पु,पू,पे,पै,पो,पौ,पं,पः,फ,फा,फि,फी,फु,फू,फे,फै,फो,फौ,फं,फः,ब,बा,बि,बी,बु,बू,बे,बै,बो,बौ,बं,बः,भ,भा,भि,भी,भु,भू,भे,भै,भो,भौ,भं,भः,म,मा,मि,मी,मु,मू,मे,मै,मो,मौ,मं,मः,य,या,यि,यी,यु,यू,ये,यै,यो,यौ,यं,यः,र,रा,रि,री,,रु,रू,रे,रै,रो,रौ,रं,रः,ल,ला,लि,ली,लु,लू,ले,लै,लो,लौ,लं,लः,व,वा,वि,वी,वु,वू,वे,वै,वो,वौ,वं,वः,श,शा,शि,शी,शु,शू,शे,शै,शो,शौ,शं,शः,ष,षा,षि,षी,षु,षू,षे,षै,षो,षौ,षं,षः,स,सा,सि,सी,सु,सू,से,सै,सो,सौ,सं,सः,ह,हा,हि,ही,हु,हू,हे,है,हो,हौ,हं,हः
'''

chars = chars.replace('\t', '')
chars = chars.replace('\n', '')
print(chars)

"""
'अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ', 'अं', 'अः', 'क', 'का', 'कि', 'की', 'कु', 'कू', 'के', 'कै', 'को', 'कौ', 'कं', 'कः', 'ख', 'खा', 'खि', 'खी', 'खु', 'खू', 'खे', 'खै', 'खो', 'खौ', 'खं', 'खः', 'ग', 'गा', 'गि', 'गी', 'गु', 'गू', 'गे', 'गै', 'गो', 'गौ', 'गं', 'गः', 'घ', 'घा', 'घि', 'घी', 'घु', 'घू', 'घे', 'घै', 'घो', 'घौ', 'घं', 'घः', 'ङ', 'ङा', 'ङि', 'ङी', 'ङु', 'ङू', 'ङे', 'ङै', 'ङो', 'ङौ', 'ङं', 'ङः', 'च', 'चा', 'चि', 'ची', 'चु', 'चू', 'चे', 'चै', 'चो', 'चौ', 'चं', 'चः', 'छ', 'छा', 'छि', 'छी', 'छु', 'छू', 'छे', 'छै', 'छो', 'छौ', 'छं', 'छः', 'ज', 'जा', 'जि', 'जी', 'जु', 'जू', 'जे', 'जै', 'जो', 'जौ', 'जं', 'जः', 'झ', 'झा', 'झि', 'झी', 'झु', 'झू', 'झे', 'झै', 'झो', 'झौ', 'झं', 'झः', 'ञ', 'ञा', 'ञि', 'ञी', 'ञु', 'ञू', 'ञे', 'ञै', 'ञो', 'ञौ', 'ञं', 'ञः', 'ट', 'टा', 'टि', 'टी', 'टु', 'टू', 'टे', 'टै', 'टो', 'टौ', 'टं', 'टः', 'ठ', 'ठा', 'ठि', 'ठी', 'ठु', 'ठू', 'ठे', 'ठै', 'ठो', 'ठौ', 'ठं', 'ठः', 'ड', 'डा', 'डि', 'डी', 'डु', 'डू', 'डे', 'डै', 'डो', 'डौ', 'डं', 'डः', 'ढ', 'ढा', 'ढि', 'ढी', 'ढु', 'ढू', 'ढे', 'ढै', 'ढो', 'ढौ', 'ढं', 'ढः', 'ण', 'णा', 'णि', 'णी', 'णु', 'णू', 'णे', 'णै', 'णो', 'णौ', 'णं', 'णः', 'त', 'ता', 'ति', 'ती', 'तु', 'तू', 'ते', 'तै', 'तो', 'तौ', 'तं', 'तः', 'थ', 'था', 'थि', 'थी', 'थु', 'थू', 'थे', 'थै', 'थो', 'थौ', 'थं', 'थः', 'द', 'दा', 'दि', 'दी', 'दु', 'दू', 'दे', 'दै', 'दो', 'दौ', 'दं', 'दः', 'ध', 'धा', 'धि', 'धी', 'धु', 'धू', 'धे', 'धै', 'धो', 'धौ', 'धं', 'धः', 'न', 'ना', 'नि', 'नी', 'नु', 'नू', 'ने', 'नै', 'नो', 'नौ', 'नं', 'नः', 'प', 'पा', 'पि', 'पी', 'पु', 'पू', 'पे', 'पै', 'पो', 'पौ', 'पं', 'पः', 'फ', 'फा', 'फि', 'फी', 'फु', 'फू', 'फे', 'फै', 'फो', 'फौ', 'फं', 'फः', 'ब', 'बा', 'बि', 'बी', 'बु', 'बू', 'बे', 'बै', 'बो', 'बौ', 'बं', 'बः', 'भ', 'भा', 'भि', 'भी', 'भु', 'भू', 'भे', 'भै', 'भो', 'भौ', 'भं', 'भः', 'म', 'मा', 'मि', 'मी', 'मु', 'मू', 'मे', 'मै', 'मो', 'मौ', 'मं', 'मः', 'य', 'या', 'यि', 'यी', 'यु', 'यू', 'ये', 'यै', 'यो', 'यौ', 'यं', 'यः', 'र', 'रा', 'रि', 'री', 'रु', 'रू', 'रे', 'रै', 'रो', 'रौ', 'रं', 'रः', 'ल', 'ला', 'लि', 'ली', 'लु', 'लू', 'ले', 'लै', 'लो', 'लौ', 'लं', 'लः', 'व', 'वा', 'वि', 'वी', 'वु', 'वू', 'वे', 'वै', 'वो', 'वौ', 'वं', 'वः', 'श', 'श, 'शा', 'शि', 'शी', 'शु', 'शू', 'शे', 'शै', 'शो', 'शौ', 'शं', 'शः', 'ष', 'षा', 'षि', 'षी', 'षु', 'षू', 'षे', 'षै', 'षो', 'षौ', 'षं', 'षः', 'स', 'सा', 'सि', 'सी', 'सु', 'सू', 'से', 'सै', 'सो', 'सौ', 'सं', 'सः', 'ह', 'हा', 'हि', 'ही', 'हु', 'ह', 'हू', 'हे', 'है', 'हो', 'हौ', 'हं', 'हः'
"""

"""
अआइईउऊएऐओऔअंअःककाकिकीकुकूकेकैकोकौकंकःखखाखिखीखुखूखेखैखोखौखंखःगगागिगीगुगूगेगैगोगौगंगःघघाघिघीघुघूघेघैघोघौघंघःङङाङिङीङुङूङेङैङोङौङंङःचचाचिचीचुचूचेचैचोचौचंचःछछाछिछीछुछूछेछैछोछौछंछःजजाजिजीजुजूजेजैजोजौजंजःझझाझिझीझुझूझेझैझोझौझंझःञञाञिञीञुञूञेञैञञोञौञंञःटटाटिटीटुटूटेटैटोटौटंटःठठाठिठीठुठूठेठैठोठौठंठःडडाडिडीडुडूडेडैडोडौडंडःढढाढिढीढुढूढेढैढोढौढंढःणणाणिणीणुणूणेणैणोणौणंणःततातितीतुतूतेतैतोतौतंतःथथाथिथीथुथूथेथैथोथौथंथःददादिदीदुदूदेदैदोदौदंदःधधाधिधीधुधूधेधैधोधौधंधःननानिनीनुनूनेनैनोनौनंनःःपपापिपीपुपूपेपैपोपौपंपःफफाफिफीफुफूफेफैफोफौफंफःबबाबिबीबुबूबेबैबोबौबंबःभभाभिभीभुभूभेभैभोभौभंभःममामिमीमुमूमेमैमोमौमंमःययायियीयुयूयेयैयोयौयंयःररारिरीरुरूरेरैरोरौरंरःललालिलीलुलूलेलैलोलौलंलःववाविवीवुवूवेवैवोवौवंवःशशाशिशीशुशूशेशैशोशौशंशःषषाषिषी                                                 ीषुषूषेषैषोषौषंषःससासिसीसुसूसेसैसोसौसंसःहहाहिहीहुहूहेहैहोहौहंहः
"""