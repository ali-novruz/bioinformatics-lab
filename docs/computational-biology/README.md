# Computational biology: modellər

### Deterministik və stoxastik baxış
Model bioloji sistemin seçilmiş hissəsinin riyazi sadələşdirilməsidir. Logistic growth dN/dt=rN(1-N/K) resurs limitini təmsil edir; exponential growth yalnız məhdud rejimdə uyğundur. Kiçik molekul sayında stochasticity orta davranışdan fərqlənə bilər.

### Gen ifadəsi modeli
dm/dt=α-βm üçün sabit vəziyyət m*=α/β-dir. Eyni steady state müxtəlif synthesis/degradation sürətlərindən yarana bilər; yalnız endpoint ölçmə parametrləri ayırmaya bilər. Time series və perturbation identifiability-ni yaxşılaşdıra bilər.

### Eksperiment
SciPy solve_ivp ilə α-nı ikiqat artırın, β sabit saxlayın; sonra α və β-ni eyni dəfə artırın. Steady state və ona çatma vaxtını müqayisə edin. Parametr confidence və ölçmə noise-u daxil etmədən mexanizm iddiası etməyin.

### Araşdırma
Problem: müşahidə eyni olan modellər. Metod: perturbation və model selection. Data: GEO time series. Zəiflik: sparse sampling. Yeni sual: hansı əlavə vaxt nöqtəsi modelləri daha yaxşı ayırır?

## Mənbə və davamı

[Rəsmi və ya ilkin mənbə](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html). [Məqalə təhlilləri](../../research/papers/README.md) və [layihələr](../../projects/README.md) ilə birlikdə oxuyun. Buradakı eksperiment sualları təklifdir, əldə edilmiş nəticə deyil.
