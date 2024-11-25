## Oppgave 1
### A:
Lambda funksjon endepunkt: https://t4dj2uv3x7.execute-api.eu-west-1.amazonaws.com/Prod/generate-image/

### B:
Github actions workflow: https://github.com/LavransFjeld/devops-eksamen-2024/actions/runs/12020378961


## Oppgave 2
### A:
Terraform apply: 
https://github.com/LavransFjeld/devops-eksamen-2024/actions/runs/12020378959/job/33508868744

### B:
Terraform plan:
https://github.com/LavransFjeld/devops-eksamen-2024/actions/runs/12020378959/job/33508868744


### SQS_QUEUE_URL:
https://sqs.eu-west-1.amazonaws.com/244530008913/image-processing-queue-30


## Oppgave 3
### A:
Tag navn: sqs-tester-client
begrunnelse: fordi det er en client som skal teste sqs-løsningene

### B:
Container image: lavransf/sqs-tester-client
SQS URL: https://sqs.eu-west-1.amazonaws.com/244530008913/image-processing-queue-30


## Oppgave 4
### A:


## Oppgave 5

#Automatisering og kontinuerlig levering (CI/CD)
Serverless-arkitektur, som AWS Lambda, tar i bruk funksjoner hver for seg som svarer på forskjellige eventer og triggere som gjør det lett å holde kontroll og endre på de forskjellige funksjonene. Mye av automasjonen skjer i stor grad gjennom CI/CD verktøy som AWS Codepipline. Serverless gjør det lett tilgjengelig og skalertbart for å lage en cloud application. Alt unntatt egendefinert buisness logikk tar AWS av seg i de forskjellige lambda funksjonene. 
Det kan være utfordringer med serverless-arkitektur når flere funksjoner blir laget blir piplinesa til hver funksjon mer kompleks. Når hver funksjon krever en pipline for testing, bygging og distrubisjon kan det føre til overhead i vedlikehlold til CI/CD-prossesen.
I mikrotjeneste arkitektur, er det vanlig å bruke containere for å holde kontroll på CI/CD. Fordelene er at for hver tjeneste har man et eget api kall som kan gjøre det lett å teste og validere. Hver tjeneste kan bli bygg og deployet hver for seg, som gjør det lett og automatisere.
Siden hver tjeneste inneholder mye kode, kan det være vanskeligere å forstå hva hver tjeneste gjør og føre til lengre byggetid og testtid.
Serverless-arkitektur gir en mer effektiv og lett deployment metode, men på kostnad av at det blir vanskeligere å kontrollere de forskjellige pipelinesene med mange funksjoner. Mikrotjenester fungerer bra hvis du liker å ha kontroll på hver tjeneste å pipline. 

#Observability (overvåkning)
I en serverless-arkitektur kan man bruke forskjellige værktøy for å få en oversikt over loggsa og om det er noen errorer. I AWS bruker man værktøy som CloudWatch til å kunne se informasjon om lambda funksjonene. 
Det er ikke alltid så lett å bruke serverless-arkitektur til å logge ettersom det ikke alltid kommer opp i CloudWatch consolen. Det kan også være vanskelig å finne hvor erroren stammer fra siden det er distribuert logging. Funksjonene er også noe som er kaldt ephemeral som betyr at de blir ødelagt og lagd igjen som kan gjøre det vanskelig å holde en god logging kontekst over flere påkallelser av funksjonen. 
Mikrotjenester sin store fordel er at den bruker containere som gjør det lett å få informasjon om system-level informasjon som CPU og lagring samtidig som logs fra selve tjenesten. Dette gjør debugging lettere hvertfall med gode api endepunkt. 
Med mange tjenester kan tracing bli komplisert ettersom hver av tjenestene kommuniserer med hverandre og det da blir vanskelig å se i loggsa når og hvem som ble triggera først. Med mange dependencies kan loggingen også bli kronglete.
Serverless arkitektur minsker infrastruktur-relaterte ansvar, men logsa er ikke alltid så godt definert og lett å finne fram til. Mikrotjenester på den andre siden har svært oversiktlig logs i consolen, men vanskeligere å trace fra hvilken tjeneste de forskjellige errorene kommer fra hvis de er sammenkoblet. 	

#Skalerbarhet og kostnadskontroll
En veldig bra ting med serverless-arkitektur er at det er automatisk skaler barhet. Det betyr at AWS Lambda funksjoner skaleres opp eller ned basert på etterspørsler. Dette kan gjøre at systemer kan håndtere plutselige trafikktopper. 
Serverless-arkitektur har en limitasjon på maksimal skalering. AWS lambda har grenser for samtidige forespørsler. Det kan føre til throttling hvis systemet har for høy belastning.
Betaling foregår ved bruk av funksjonen, som vil si at det blir betalt med hvor mange som bruker funksjonen fks(antall forespørsler). Det blir derfor billigere når det ikke er så mange som bruker funksjonen, noe som vil gjøre det billigere enn å ha noe som alltid er på. Budsjettering kan bli vanskeligere med tanke på ujevnheten som blir gjort av skaleriteten.
Siden mikrotjenester bruker container kan de justere skalerbarheten med andre verktøy til containerene som kan skaleres basert på forskjellige parametere. Dette gjør det mulig å definere skaleringer for hver tjeneste. 
Det er ofte mer forutsigbart med kost for antall tjeneste ettersom hver tjeneste og ressurs er separert hver for seg. Siden resursene blir optimalisert for konstant ytelse gir det en klar fordel. Det kan også være smart å ha ekstra tjenester som sikkerhetsmargin, noe som øker faste kostnader.
Serverless-arkitektur er automatisk, hvor AWS gjør mye av jobben for deg med tanke på skalering.  Dette eliminerer kosten av ledig ressurser. Mikrotjenester har mer kontroll over skalerings strategiene sine, det kan også være billigere når man har kontroll over hver tjeneste. 

#Eierskap og ansvar
I en serverless-arkitektur er det ikke så mye ansvar på teamet ettersom AWS tar seg av ressurser som servere, operativsystemer og nettverkskonfigurasjoner. Dette gjør det lett for utviklerne å fokusere mer på logikken rundt applikasjonen og busniess funksjonaliteten. Det kan være en stor fordel for startups, eller små teams. 
Siden ansvaret er lavt betyr det at teamet får mindre kontroll. De må stole på at AWS sikrer pålitelighet, sikkerhet og ytelse som kan bli problematisk om det skulle komme problemer i infrastrukturen til leverandøren. Det er også viktig med kostnadene som teamsa må passe på for å forhindre uventende kostnader fra dårlig optimaliserte funksjoner eller uforutsette trafikkmønstre.
Når det kommer til applikasjons ytelse, så er hovedfokuset på å optimalisere funksjonene design og dependencies mellom funksjonene. Det kan bli vanskelig å finne errorer i serverless arkitektur, hvert fall hvis det er mellom flere tjenester som SQS og lambda. 	
I mikrotjenester har devops team full kontroll over ansvaret for både infrastrukturen og applikasjon ytelsen. Hver tjeneste er containeriezed som blir gjort via docker, som gir felksibilitet og ressurs bruk til forskjellige behov. 
Kontrollen den kommer med kompleksitet. Man burde være erfaren og ha ressurser når man skal administrere infrastrukturen, sikkerhet og scaling. Hvis det skulle skje et ytelsesproblem i tjenesten, så er teamet ansvarlig for å diagnostisere problemet, uansett om det er feil med koden, mangel på ressurs eller infrastruktur feil. Man burde derfor ha mange devops ressurser. 
Mikrotjenester har også et klarere syn på kost. Man kan administrere ressursbruk og optimalisere for spesifikke behov, men det kan lede til individuelt team som prioriterer tjenesten uten tanke på hele systemet. 
Serverless-arkitetktur gjør at man ikke trenger å fokusere så mye på infrastruktur, men mer ansvar for ytelse og kostnadsstyring til applikasjonsnivå. Så hvis man har lyst til å prioritere funksjonaliteten og bruke mindre tid på infrastruktur er det smart med serverless. Med mikrotjenester får man god kontroll over infrastrukturen og applikasjons ytelsen, men man trenger en god forståelse og riktige ressurser for å opprettholde effektiv drift.

#Kilder:
https://medium.com/@tarekbecker/a-production-grade-ci-cd-pipeline-for-serverless-applications-888668bcfe04
https://www.enov8.com/blog/serverless-architectures-benefits-and-challenges/
https://medium.com/@dmosyan/ci-cd-for-microservices-1b5582f3e1fd
https://www.tatvasoft.com/outsourcing/2024/06/microservices-vs-serverless.html
https://lumigo.io/serverless-monitoring/serverless-logging/
https://genezio.com/serverless-scalability/
https://medium.com/cloud-native-daily/scaling-microservices-a-comprehensive-guide-200737d75d62
https://www.cloudflight.io/en/blog/the-hidden-cost-of-microservices-and-how-to-overcome-them/
https://medium.com/@use.abhiram/serverless-computing-and-shared-responsibility-a-comprehensive-guide-4a30cef4b23b
https://www.osohq.com/learn/microservices-best-practices





