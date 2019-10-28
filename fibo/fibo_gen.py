class Fibo:

    def fibo_gen(self, quantity):
        results = [0, 1]
        tmp1, tmp2 = 0, 1
        tmp_res = []
        for i in range(1, quantity):

            tmp1, tmp2 = tmp2, tmp1 + tmp2
            tmp_res.append(tmp2)

            result = results[i-1] + results[i]
            results.append(result)

        print(tmp_res)
        print(results)

f = Fibo()
f.fibo_gen(7)
