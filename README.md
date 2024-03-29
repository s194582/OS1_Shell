62588 - OS ASSIGNMENT 1: SHELL


VEJLEDNING:
Vores shell kan køres på UNIX baserede systemer. Med dette tænkes der på MacOS og Linux distributions.
Start med at downloade filen, og gem den i den ønskede mappe.
Åben derefter terminalen, og brug de nødvendige system calls/kommandoer til at komme ind i den rette mappe.
De systems calls der tænkes på, er:

ls - bruges til at få en liste over de dokumenter og mapper i det directory man befinder sig i.

cd directory - cd bruges til at ændre directory. Ved at bruge cd kommandoen, kan man åbne en mappe, og se hvad der er i den pågældende mappe. Et eksempel på et cd 
kald kan være, at hvis man ønsker at komme ind i download mappen, så ville man kunne skrive: cd Downloads

pwd - Viser hvilket directory man befinder sig i.

Når man via terminalen har navigeret sig til den rette mappe, hvor filen ligger, kan filen køres ved at bruge kommandoen:
python3 Assignment1New.py
Når filen er kørt, er det muligt at bruge unix commands til at navigere i den nye shell.
Ønsker man at afslutte filen, kan dette gøres på følgende to måder:
Ctrl + c
indtast: exit







I/O REDIRECTION:
UNIX baserede styresystemer har indbygget en række værktøjer, til at effektivisere brugen af systemet. Et af disse værktøjer er I/O redirection, som hjælper med at distribuere systemets forskellige former for input og output. 

Linux terminalen har tre redirection funktioner. Standard input - stdin, standard output - stdout og standard error -stderr som er en fejlbesked som terminalen outputter hvis en process har fejlet. 

Standard input anvendes f.eks. i forbindelse med at føre data fra systembrugeren til software. Standard inputtet eksekveres når der ikke er mere data at indlæses, dvs når EOF nås. Dette kan eksempelvis være via tastatur input.   

Standard output fungerer lidt som modsætningen af Standard input, hvor at inputtet er hvad der går fra brugeren til software, er output hvad der går fra softwaren og til terminalen. 

Standard error anvendes når noget software forårsager en fejl, som så redirectes gennem standard error til systemets terminal. 


CONCEPT OF SYSTEM CALLS:

System Calls kan overordnet gruppes ind i seks kategorier:
file systems, process, scheduling, interprocess communication, socket (networking) and miscellaneous.
System Calls bruges under en process til, at en process kan bede om en specifik service fra kernel.
Eksempler fra programmet vi har lavet, er fork(), wait() og dup2().


THE PROGRAM ENVIRONMENT:
Den shell vi har programmeret, er programmeret på linux baserede operating systems. Dette har været en nødvendighed, da når man arbejder med Shell, er man nødsaget til at arbejde på operativ systemer der bygger oven på unix systemet.
Dette er en nødvendighed, da de system calls vi bruger, er skrevet til unix systemet. 
Nu til dags, når man snakker unix baserede systemer, tænker man på to operating systems: MacOS og Linux baserede operating systems. 



BACKGROUND PROGRAM EXECUTION:
I det den programmeret shell bliver kørt, er det første der sker, at python libraryet “os” hentes.
Herefter bliver funktionerne “cd()”, “command()” og “pipe()” defineret til senere brug i kørslen af programmet.
Efter at funktionerne er defineret, gåes der ind i et while-loop, der er sat op således, at det aldrig afslutter, medmindre den specifikt bliver bedt om det.
Når programmet er gået ind i while-loopet, beder programmet om et user input, som det gemmer som en variable. Ved manipulation med variablen, Splitter den og gemme den som en ny variable, er det muligt at undersøge hvilket slags input der er blevet givet i terminalen.
Programmet undersøger om der er tale om “exit” commandoen, “cd” commandoen eller en “pipe” command.
Hvis det ikke er en af disse tre commandoer der bliver kaldt, er der i stedet tale om en internal command, og funktionen Command() bliver kaldt.
Ud fra hvilken command der bliver kaldt i terminalen, kan man nedenstående læse hvad der sker i den bagvedliggende logik.

COMMAND:
Når der bliver kaldt en internal command i terminalen, kaldes funktionen Command(). I Command() startes der med at forkes via en defineret variable, i programmet defineret som “rc”. Når der er blevet forket, blives der ved hjælp af to if statements undersøgt, hvilken process der er child og hvilken process der er parent. I parent processen bruges system called os.wait. Ved brug af dette system call, fortælles parent processen, at den skal vente med at kører, indtil child processen er færdiggjort. Imens der bliver kaldt wait() i parent processen, kører child processen stadig væk. 
Inden i child processen bliver system call “os.execvp()” kaldt, med de tilhørende argumenter, hvorefter den kører og printer den commando, der er blevet kaldt i terminalen.
Når “os.execvp()” afslutter, terminerer den også, den process den er blevet kaldt i. Dermed afsluttes child processen, hvilket giver parent processen mulighed for at kører færdig. dermed afsluttes funktionen Command(), og der gåes tilbage til while-loopet, der kører tilbage til start, og beder om et nyt input fra brugeren.


PIPE:
Først checker koden for kommandoen ‘|’. Derefter splitter den de to kommandoer på hver side af pipe kommandoen. Hvis man for eksempel inputter “ls -a | wc” gemmes de to kommandoer ned i et array nemlig [ls -a] og [wc].
dernæst køres fork funktionen  hvori parent process bliver stallet med en wait() statement indtil child processen er færdig. I child processen defineres desctiptors til pipen. Disse descriptors er hvad der senere bliver til input af røret og output af røret. Dernæst køres der endnu en fork() i child processen for at duplikerer røret OG for at programmet skal fortsætte efter der bliver kørt exec() funktionen senere. I child processen lukkes der for read desriptoren, den får vi ikke brug for her. Ydermere køres dup2 med parameterne writeDescriptor og STDOUT som gør at processens writedescriptor bliver kopiret over i STDOUT så outputtet ikke bliver smidt til skærmen, men i stedet bliver linket til den anden ende af røret. Det samme gentager sig for writeDescriptoren bare i den næste child process. Til sidst køres exec() hvor outputtet fra venstre side af ‘|’ bliver smidt over i kommandoen fra højre side som input. alle child processer bliver dræbt og parent kører videre som normalt. 

CD:
Hvis strengen matcher cd i programmet bliver funktionen cd kørt med kommandoen efter cd i inputtet som parameter. Programmet checker om kommandoen er over 1 argument for hvis den er det skifter den director med den indbyggede os funktion chdir. Hvis ikke der er 1 argument går vi til home directorien med chdir(os.environ[“Home”]) som pointer til brugeren login directory. 

EXIT:
Hvis der i user input er blevet kaldt, bruges statementet break til at terminere while loopet. dette gør at den breaker parent loopetet, således programmet køres færdigt. 
