# Dərs planı

## Dərsin nəticəsi

Dərsin sonunda tələbə gen ifadəsi matrisini izah edir, yüksək ölçülü datada sızma riskini göstərir, balanced accuracy ilə accuracy arasındakı fərqi tətbiq edir və permutation nəzarətinin nəyi sınadığını düzgün ifadə edir.

## Hazırlıq

- Repo quraşdırılıb və `biolab list` işləyir.
- Müəllim saxlanmış nəticələri göstərmək üçün internetə ehtiyac duymur.
- Canlı icra planlaşdırılırsa, Khan CSV-ləri əvvəlcədən endirilir və ya şəbəkə yoxlanılır.
- Təqdimatın `Slide Show` rejimi və danışıq qeydləri əvvəlcədən açılır.

## 50 dəqiqəlik dərs

| Vaxt | Mövzu | Müəllimin işi | Tələbənin işi |
|---:|---|---|---|
| 0–5 dəq | Bioloji sual | Dörd sinifli təsnifat problemini və datasetin sərhədini təqdim edir | Hansı sübutun klinik qərar üçün çatmadığını qeyd edir |
| 5–12 dəq | Data quruluşu | 63×2308 training və 20×2308 test matrisini izah edir | Nümunə və xüsusiyyət oxlarını müəyyən edir |
| 12–20 dəq | Sızmasız pipeline | Feature selection-un hər fold daxilində aparılmasını göstərir | Sızmalı alternativdə problemin harada yarandığını tapır |
| 20–28 dəq | Model seçimi | `k` və `C` grid-i, stratified CV və balanced accuracy-ni izah edir | Accuracy ilə balanced accuracy-ni müqayisə edir |
| 28–36 dəq | Test nəticəsi | Confusion matrix və 19/20 nəticəsini şərh edir | Yeganə səhvi yazır və macro F1-i izah edir |
| 36–43 dəq | Mənfi nəzarət | Nested CV-ni 99 permutation nəticəsi ilə müqayisə edir | p=0.01-in bu eksperiment daxilində mənasını yazır |
| 43–47 dəq | Məhdudiyyət | Kiçik test, tarixi preprocessing və naməlum probe adlarını müzakirə edir | Qəbul edilməyən bir iddianı müəyyən edir |
| 47–50 dəq | Yekun sual | Növbəti müstəqil cohort planını soruşur | Bir cümləlik follow-up eksperiment təklif edir |

## 90 dəqiqəlik laboratoriya əlavəsi

1. `biolab run expression-ml` əmrini işlədin.
2. Yeni run qovluğunda `run.json` və `summary.json` fayllarını açın.
3. `predictions.csv` faylında səhv nümunəni tapın.
4. `cv_results.csv` daxilində eyni maksimum bala çatan parametrləri müqayisə edin.
5. `selected_probes.csv` nəticəsini gene symbol siyahısı kimi təqdim etməyin. Səbəbini dataset kartı ilə əsaslandırın.
6. Training-only nəzarət nəticəsini açın və real score-u null paylanma ilə müqayisə edin.

## Qiymətləndirmə rubrikası

| Meyar | Bal |
|---|---:|
| Dataset, train/test bölgüsü və xüsusiyyət sayının düzgün izahı | 20 |
| Pipeline və data sızması riskinin düzgün izahı | 25 |
| Metriklər və confusion matrix şərhi | 20 |
| Permutation nəzarəti və p-value şərhi | 20 |
| Məhdudiyyət və növbəti eksperiment | 15 |
| **Cəmi** | **100** |

