author: Ir1d, Planet6174, abc1763613206, StudyingFather, cjsoft, Marcythm, luoguyuntianming, ChungZH, Xeonacid, YZircon, i-Yirannn, H-J-Granger, NachtgeistW, YuzhenQin, Andycode3759, HHH2309, shigengxin123456, Re-Ori, hcx1204

## Event overview

**The Olympiad in Informatics** (OI) is a subject competition widely conducted among secondary school students, of the same nature as competitions in physics, mathematics, and so on. What OI examines is contestants' ability to solve practical problems by writing computer programs using knowledge of algorithms, data structures, and mathematics.

There are many kinds of OI competitions; in China alone they include:

-   The National Olympiad in Informatics in Provinces (NOIP)
-   The National Olympiad in Informatics (NOI)
-   The National Olympiad in Informatics Winter Camp (WC)
-   The China Team Selection Contest for the International Olympiad in Informatics (CTSC)

International OI competitions include:

-   The International Olympiad in Informatics (IOI)
-   The USA Computing Olympiad (USACO)
-   The Japanese Olympiad in Informatics (JOI)
-   The Asia-Pacific Informatics Olympiad (APIO)

    ……

For most contestants, each year's new season begins with the first round of CSP-J/S in September.

In China, the only language allowed in OI competitions is C++ (C and Pascal were once also available, but support has been discontinued). Different competitions have different rules about the version of C++. Contest problems are generally related to algorithms or data structures, and the problem formats include traditional problems (the most common, which specify input from and output to files) and non-traditional problems (answer-submission problems, interactive problems, code-completion problems…… and so on).

## Format overview

### The OI format

Contestants have only one submission opportunity. Judging results cannot be seen during the contest; scores are announced after the contest. Each problem has multiple test points, and one earns a corresponding score based on the number of test points passed for each problem; each test point may also have partial credit, so points can be earned even if only part of the data passes.

???+ note "The self-evaluation tool selfEval"
    Nowadays, some NOI-series contests provide the selfEval self-evaluation tool. selfEval is built into the national-contest customized edition of NOI Linux. Since it was officially announced and put into use at NOI 2023, selfEval has been progressively used in subsequent NOI national contests, APIO (China region), the NOI Winter Camp, and so on. Contestants can use selfEval to test their programs on a set of test data (called pretest data) and get feedback. The number of self-tests a contestant can do in each contest has a specified upper limit (the self-test limit for NOI2024 was 50 times, and for NOI2025 it was 30 times), and the pretest data is also invisible to contestants. Since the pretest data differs from the official test data, the self-test result is used only for debugging and cannot be regarded as an official judging score. When a contestant does multiple pretests on the same problem, the pretest data used is the same.

CSP-J/S round two, NOIP, provincial selection, and NOI all use the OI format.

### The IOI format

Contestants have multiple submission opportunities during the contest. The contest judges in real time and returns results; if a submission's result is wrong, there is no penalty. Each problem has multiple test points, and one earns a corresponding score based on the number of test points passed for each problem.

APIO and IOI both use the IOI format. Currently, domestic competitions are also gradually moving toward the IOI format.

### The Codeforces (CF) format

[Codeforces](https://codeforces.com) is an online judge system that regularly holds contests.

A feature of its contests is that during the contest only part of the data (Pretests) is tested, while after the contest the full results of all test points (System Tests) are returned. During the contest one can submit multiple times and is allowed to Hack others' code (here Hack means submitting a test case that makes another's code fail to give the correct answer). To Hack, a contestant must lock their own code (in other words, they cannot resubmit that problem during the contest). During Hacking one is not allowed to copy the contestant's program locally for testing; the source code is converted into an image.

Codeforces also provides another format, called Extended ICPC (or ICPC+). In this format, all data is tested during the contest, but after the contest there is a 12-hour open Hack period for everyone. During Hacking in this format, one is allowed to copy the contestant's program locally for testing.

## Major competitions

### CSP-J/S

**CSP-J/S** (Certified Software Professional Junior/Senior) is a non-professional-level software capability certification test set up by CCF after NOIP was cancelled in 2019; before 2025 it was open to all ages, and [was later changed to 12 years and older](https://www.noi.cn/xw/2025-02-13/837984.shtml).

CSP-J/S is divided into two groups, the entry level (Junior, abbreviated CSP-J) and the advanced level (Senior, abbreviated CSP-S); the schedule is divided into round one (generally in September each year) and round two (generally in October each year). Round one is a written test examining computer theory, common operational knowledge, and basic algorithm and mathematics knowledge; round two is an on-machine test, with 4 problems for both the entry and advanced groups, where the entry group has a 3.5-hour exam and the advanced group a 4-hour exam (except CSP-S 2019, which used the old NOIP advanced-group format, with the schedule divided into two days, 3 problems and 3.5 hours per day). Round one is open to all students aged 12 and above from society; after a certain ranking-based filtering, those with excellent scores have the opportunity to take round two.

Registering for round one/two, and filing problem appeals after round two, all require paying a fee to CCF.

Both rounds of testing certify contestants' scores by rank on a per-province basis, graded into first, second, and third classes.

### NOIP

**NOIP** (National Olympiad in Informatics in Provinces) is an informatics competition organized by the People's Republic of China for Chinese (including Hong Kong and Macau) secondary school students.

The old format in 2018 and before: NOIP was divided by participant group into the popular group and the advanced group, and an entry group was piloted in Shanghai in 2018; by stage it was divided into the preliminary round and the final round. The preliminary round examined some computer fundamentals and algorithm basics, and the final round was an on-machine test. In terms of timing, it was generally the second weekend of November: Saturday morning the advanced group round one 8:30-12:00 (3.5 hours, 3 problems total), afternoon 14:30-18:00 the popular group (3.5 hours, 4 problems total), Sunday morning the advanced group round two 8:30-12:00 (3.5 hours, 3 problems total). The whole country used the same set of papers, but the award rules were uniformly specified by CCF (China Computer Federation) according to the situation within each province and announced after the contest on the [NOI official website](http://www.noi.cn). The first-prize score line differs slightly by province.

NOIP was [suspended by CCF](http://www.noi.cn/xw/2019-08-16/715365.shtml) on August 16, 2019, and was [announced restored](http://www.noi.cn/xw/2020-01-21/715520.shtml) on January 21, 2020. The NOIP format from 2020 onward differs from before, specifically as follows:

-   The preliminary round was cancelled and replaced by CSP-J/S round one;
-   The popular group was cancelled and replaced by CSP-J; thereafter NOIP has only one group, aimed at advanced-group-level contestants;
-   The schedule was reduced from the previous two days with 6 problems total and 3.5 hours per day, to one day with 4 problems and 4.5 hours total.
-   Contestants must achieve a certain ranking in CSP-S round two to qualify for NOIP; the specific quotas differ by province. A province's NOIP participation quota is related to that province's number of participants and results in the previous season.

Registering for NOIP and filing problem appeals do not require an extra fee.

NOIP ranks and awards on a per-province basis. As of 2019, contestants at most universities who won an advanced-group provincial first prize could obtain independent-admission qualification.

> In January 2020, the Ministry of Education of the People's Republic of China issued the [Opinions on Carrying Out a Pilot Reform of Basic-Discipline Admissions at Some Universities](http://www.moe.gov.cn/srcsite/A15/moe_776/s3258/202001/t20200115_415589.html). The opinions stated that from 2020, independent university admissions would no longer be organized, and a pilot reform of basic-discipline admissions (the "Strong Foundation Plan") would be carried out at some world-class universities under construction.

### Provincial team selection

**Provincial team selection** (in short, provincial selection) is used to select each province's representative team for the national contest, generally held from January to April each year. The schedule is generally divided into two days, with 3 problems and 4.5 hours per day.

The problems for provincial selection are decided by each province itself; the current trend is that many provinces choose to set problems jointly.

Each provincial team's quota has a complex calculation formula, generally related to previous results and the number of participants. Generally, NOIP scores need to account for a certain proportion in the metrics of provincial selection. According to the rules, junior-high contestants can only be selected as Class-E contestants and cannot participate in Class-A or Class-B selection. There are 5 Class-A contestants ([at least 1 female](https://www.noi.cn/xw/2024-08-26/829152.shtml)), and the other contestants enter the Class-B team in order according to the given quota and their scores. A single school's quota for participating in NOI does not exceed one-third of the total Class-A and Class-B quota of its province (rounded), and the highest-scoring female contestant selected into the Class-A team does not count toward this proportion (in short, the 1/3 restriction or 1/3 elimination; for details see the [official CCF explanation](https://www.noi.cn/xw/2022-12-14/781364.shtml)).

From 2020, NOI provincial team selection was uniformly set and judged by CCF; provinces capable of setting problems could set their own, but the selection method had to be approved by CCF. From 2024, NOI provincial team selection returned to each province setting its own problems; provinces with such needs could organize joint exams or use other provinces' papers, but the specific plan had to be approved by CCF.

### NOI

**NOI** (National Olympiad in Informatics) is the highest-level competition for provincial representative teams within China, including Hong Kong and Macau.

NOI is generally held in July, and contestants are divided into two categories: official contestants and summer-camp contestants. Official contestants are further divided into three classes, of which Classes A and B are official provincial-team contestants, and Class-C contestants are invitational contestants. Classes A and B correspond to the province's Class-A and Class-B contestants (of which Class A gets a 5-point bonus when computing scores); Class C is nominally a reward quota for a school after making an outstanding contribution to CCF. Summer-camp contestants are divided into Classes D and E, corresponding respectively to high-school and junior-high contestants participating as unofficial contestants. If a summer-camp contestant's score exceeds the score line, they only get a score certificate but no medal (the same score is somewhat less valuable). The top 50 official contestants form the National Training Team and obtain recommended-admission qualification.

On international platforms, to distinguish it from other competitions also called NOI, it is sometimes called CNOI.

### CTT

**CTT** (China Team Training) is a training and selection activity held each winter for National Training Team contestants for IOI, consisting of 3-4 tests. Besides the National Training Team, some contestants who achieved excellent results in that year's NOI may also participate in CTT under the name of "elite training".

CTT, together with other processes such as regular assignments, forms the first stage of national team selection. From 2021, the top 30 contestants in the first-stage ranking become the National Candidate Team and enter the second stage of selection (WC).

### WC

**WC** (Winter Camp, the National Olympiad in Informatics Winter Camp) is an activity held each winter at that year's NOI host location. Although the activity is mainly used for Training Team training and national team selection, contestants who achieved good results in the previous year's NOIP and CSP-S round two may also participate as unofficial campers.

WC's content includes several days of training and testing; the test scores are aggregated with results from prior stages to compute the comprehensive ranking of Training Team contestants. Before 2020, there was only one test, and the Training Team and unofficial campers had the same test problems; the top 15 in the Training Team's comprehensive score became the National Candidate Team and participated in the final stage of selection (CTS, etc.). From 2021, as CTS's national-team-selection function was merged into WC, the National Candidate Team's test became two sessions, while unofficial campers still had one test, and the unofficial campers' test problems partly overlapped with the candidate team's test problems. The top 6 in the candidate team's comprehensive ranking enter the final interview, and 4 official contestants and 2 substitute contestants are selected to participate in that year's IOI.

### APIO

**APIO** (Asia-Pacific Informatics Olympiad) is an informatics subject competition for secondary school students in the Asia-Pacific region. CCF holds a China-region mirror contest in early May each year. There are training activities around the contest day.

APIO contestants can be divided into Class A and Class B; the top six (including ties) among Class-A contestants can participate in the international award evaluation of APIO, while Class-B contestants can only participate in the China-region award evaluation.

### CTS

**CTS** (formerly CTSC, China Team Selection Competition) is used to select the national team (6 people) from the National Candidate Team (15 people) to prepare for that summer's IOI, with 4 official contestants and 2 substitute contestants. Like WC, contestants who achieved good results in the previous year's NOIP may also participate (without taking part in selection).

Both APIO and CTS register on a per-province basis, and the participants for APIO and CTS are generally determined by ranking based on NOIP scores (the two are generally very close in time).

The 2020 CTS was cancelled due to the pandemic, and that year's National Training Team was selected through NOI; from 2021, the CTS selection process was replaced by WC.

### IOI

**IOI** (International Olympiad in Informatics) is an annual informatics subject competition for secondary school students worldwide. Each country has four contestants, and the contest is generally live-streamed. In the IOI format, each problem has subtasks, and each subtask corresponds to a certain score.

### Subject camps

#### Peking University (PKU)

-   Peking University Winter Informatics Experience Camp (PKUWC): held around the Winter Camp.
-   Peking University Informatics Experience Camp (PKUSC): generally held on campus in June. Since the contest is in the school's computer lab, the lab environment is Windows and the contest system is OpenJudge.
-   Peking University Secondary-School Summer Class (Informatics): held during summer vacation, aimed at second-year high-school science students.

#### Tsinghua University (THU)

-   The Computer Science Department "Secondary-to-University Bridging" Winter Seminar and Teaching Activity: equivalent to the Informatics Winter Camp, sometimes abbreviated in English as THUWC. Generally two days: the mornings are competitions (the first day is a standard OI contest, the second day is Tsinghua's original "engineering problem" contest), and the afternoons are course training.

## OI competitions in other countries and regions

### USA: USACO

Official website: <http://www.usaco.org/>

USACO is perhaps the foreign OI competition most familiar to domestic contestants (and possibly the foreign OI competition with the most Chinese editorials).

Each year from winter to early spring, USACO holds one online contest per month. A contest lasts 3-5 hours.

According to the official website, USACO's contests are divided into these 4 difficulty divisions (3 divisions before the 2015-2016 school year):

-   Bronze, suitable for programming beginners, especially students who have only learned the most basic algorithms (such as sorting, binary search);
-   Silver, suitable for students beginning to learn basic algorithmic techniques (such as recursion, search, greedy algorithms) and basic data structures;
-   Gold, where students encounter more complex algorithms (such as shortest paths, DP) and more advanced data structures;
-   Platinum, suitable for contestants with solid algorithm-design ability; Platinum can help them challenge themselves with complex and more open-ended problems.

In China, the OJ platform with the most complete set of USACO problems is currently Luogu.

### Poland: POI

Official website: <https://oi.edu.pl/>

Official submission address: <https://szkopul.edu.pl/p/default/problemset/>

POI is a foreign OI competition that many provincial-selection contestants practice most.

According to the [POI official website](https://oi.edu.pl/l/42/), POI's process is as follows:

-   Round one: six problems (five for the 31st edition and before), online contest;
-   Round two: includes one practice contest and two official contests, where the practice contest has one problem and each official contest has two problems;
-   Round three: includes one practice contest and two official contests, where the practice contest has one problem and each official contest has three problems.

In some years, a contest called ONTAK was held, whose official name is the POI training camp, benchmarked against China's National Training Team training contest (CTT).

In addition, Poland also holds a public contest called PA, roughly meaning "battle of algorithms", whose official website is: <https://potyczki.mimuw.edu.pl/>.

Currently among domestic OJs, the one with the most complete POI problems is BZOJ.

### Croatia: COCI

Official website (English): <http://www.hsin.hr/coci/>

Official website (Croatian): <http://www.hsin.hr/honi/>

A contest with a very wide difficulty span, roughly from popular- to provincial-selection-.

In the past, all COCI problems provided the statement, data, editorial, and reference solution. From the end of 2017, COCI's editorials and reference solutions stopped being updated. In the 2019-2020 season, updates of editorials and reference solutions restarted.

Luogu, BZOJ, and LibreOJ all have a small number of COCI problems.

### Japan: JOI

Official website: <https://www.ioi-jp.org/>

JOI (Japanese Olympiad in Informatics) provides the statement, data, editorial, and reference solution for all problems. The JOI Final and Spring Camp of the past two years provided English statements, but no English editorials. All past JOI Open contests provided English versions of the statements and editorials.

JOI's process:

-   Qualifying round (予選)
-   Final round (本選 / JOI Final)
-   Spring Camp (春季トレーニング合宿 / JOI Spring Camp / JOISC)
-   Open Contest (通信教育 / JOI Open Contest)

The qualifying round is relatively easy; from the 2019/2020 season, the qualifying round has multiple rounds. The difficulty of JOI Final ranges from about advanced- to advanced+. The difficulty of JOISC and JOI Open problems ranges from advanced to NOI-.

The vast majority of JOI problems can be submitted at [AtCoder](https://atcoder.jp/). You can find more JOI problems (Japanese statements) on the JOI official website or on AtCoder.

Currently LibreOJ and BZOJ have JOI Final, JOISC, and JOI Open problems from recent years.

### Russia: ROI

Official website: <http://neerc.ifmo.ru/school/archive/index.html>

Online submission address: <https://contest.yandex.ru/roiarchive/> and Codeforces (partial).

ROI (Russian Olympiad in Informatics) is Russia's informatics competition.

Process:

-   Municipal Stage (Муниципальный этап)
-   Regional Stage (Региональный этап)
-   Final Stage (Заключительный этап)

Currently LibreOJ has translations of recent years' ROI final-round problems.

Besides this, other larger Russian competitions for secondary school students include:

-   Internet Informatics Olympiads (Интернет-олимпиады по информатике)
    -   Official website: <http://neerc.ifmo.ru/school/io/index.html>
    -   This contest is held by ROI problem setters.
-   All-Russian Team Informatics Olympiad for School Students (Всероссийской командной олимпиады школьников)
    -   Official website: <http://neerc.ifmo.ru/school/russia-team/index.html>
    -   This contest's qualifier, the Moscow Team Olympiad, can be submitted on Codeforces.
-   Innopolis Open
    -   Official website: <https://olymp.innopolis.ru/en/ooui/information/>
-   Open Olympiad in Programming for School Students (Открытая олимпиада школьников по программированию)
    -   Official website: <https://olympiads.ru/zaoch/>
    -   The official website says this contest is benchmarked against ROI.

### Canada: CCC & CCO

CCC (Canadian Computing Competition) and CCO (Canadian Computing Olympiad): you can look up information and problems from past editions on their [official website](https://cemc.math.uwaterloo.ca/contests/past_contests.html#ccc).

You can submit [CCC](https://dmoj.ca/problems/?category=4) and [CCO](https://dmoj.ca/problems/?category=24) on DMOJ, which also has CCC editorials.

CCC Junior/Senior is close to the NOIP popular/advanced group difficulty. Winning a gold medal at CCO may require the level of an NOI silver medal.

### Singapore: NOI SG

Official website: <https://noisg.comp.nus.edu.sg/noi/>

Its full name is Singapore National Olympiad in Informatics, and in the Singaporean domestic context, where no ambiguity arises, it is also called NOI. In terms of format, it is divided into the Online Qualification Contest and the Final Contest. The Online Qualification Contest is registered on a per-school basis; contestants participate at their own school and submit remotely over the network. Qualifying-round scores are ranked only within the school, and the top 5 non-zero-scoring contestants qualify to participate in the Final Contest as school representatives.

Currently domestic OJs' inclusion of NOI SG problems is rather scarce; you can find past-year statements, test data, and official standard programs on the [official GitHub account](https://github.com/noisg).

### Taiwan region: Informatics Olympiad

The Taiwan region translates "informatics" in OI as「資訊」rather than the mainland's common translation「信息」.

If a contestant from the Taiwan region wants to participate in IOI, they must go through these rounds:

-   Regional Informatics Aptitude Competition
-   National Informatics Aptitude Competition
-   Informatics Study Camp (TOI)

### Other countries

-   Australia: AIO: <https://orac.amt.edu.au/hub/aio/>

    -   Difficulty similar to NOI.

-   UK: British Informatics Olympiad: <https://www.olympiad.org.uk/>

    -   Difficulty too low.

-   Czech Republic: Matematická olympiáda–kategorie P: <http://mo.mff.cuni.cz/p/archiv.html>

-   Romania: Olimpiada Nationala de Informatica: <http://olimpiada.info/>
    -   For statements, test data, and editorials, look in the tabs containing the word "Subiecte".

## Other international OI competitions

### BalticOI

**BalticOI** is aimed at the countries around the Baltic Sea. The participating countries of BalticOI 2018 included 9 countries such as Lithuania, Poland, Estonia, and Finland. The problems are hard.

Except for 2017, BalticOI publishes statements, test data, and editorials every year. BalticOI does not have a fixed official website; each year's host builds a new site. For the official websites of past years, see this [post](https://loj.ac/article/416).

Currently LibreOJ has nearly ten years of BalticOI problems.

### BalkanOI

**BalkanOI** is aimed at the countries around the Balkan region. The participating countries of BalkanOI 2018 included 12 countries such as Romania, Greece, Bulgaria, and Serbia. The problems are hard.

BalkanOI publishes statements, test data, and editorials only in certain years; for the official websites see this [post](https://loj.ac/article/416).

### CEOI

The participating countries of CEOI 2018 partly overlap with the two competitions above, including Poland, Romania, Georgia, Croatia, and others. The problems are hard.

CEOI publishes statements, test data, and editorials every year; for the official websites see this [post](https://loj.ac/article/416).

### eJOI

**eJOI**'s full name is the European Junior Olympiad in Informatics. Participating countries include Russia, Armenia, Bulgaria, Poland, and others. The problems are relatively hard.

eJOI publishes statements, test data, and editorials every year; for the official websites see this [post](https://loj.ac/article/416).

### NOI

???+ warning "Warning"
    What is introduced here is not the "National Olympiad in Informatics".

**NOI**'s full name is the Nordic Olympiads in Informatics.

Official website: <http://nordic.progolymp.se>

A competition that only started being held in the past couple of years, aimed at the Nordic countries.

## References

-   [ICPC/CCPC events and formats](./icpc.md)
-   ["Translation group" Addresses of some continental-level OI competitions](https://loj.ac/article/416)
