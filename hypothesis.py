import scipy.stats as stats
group1 = [25, 30, 28, 35, 32]
group2 = [20, 22, 18, 25, 28]

t_stat, p_value = stats.ttest_ind(group1, group2)

print(f'T-statistic: {t_stat}')
print(f'P-value: {p_value}')

if p_value < 0.05:
    print('Reject the null hypothesis')
else:
    print('Fail to reject null hypothesis')