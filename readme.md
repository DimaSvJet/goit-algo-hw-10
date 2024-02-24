Висновки
за результатов виконання програмного коду було отримано наступні результати:
1) err = 2.960594732333751e-14 - оцінка похибки при чисельному обчислені певного інтегралу функції y = x^2 на інтервалі ві а до в. В даному випадку значення полибки майже дорівнює нулю. Що вказує на дуже низьку оцінку похибки.
2) result = 2.666666666666667 - результат чисельного обчислення інтегралу функції y = x^2 (теоритична площа фігури)
3) mc_results = 2.6752 - оцінка значення інтегралу з використанням методу Монте-Карло. Результати обчислення інтегралу функції y = x^2 методом Монте-Карло відрізняються від результатів, отриманних методом integrate.quad(), так як метод Монте-Карло є статистичним методом і його точність задежить від кількості згенерованих випадкових точок. В нашому випадку результати методу Монте-Карло практично співпадають з методом integrate.quad().
4) Результат, отриманий методом Монте-Карло є достаньо точним.