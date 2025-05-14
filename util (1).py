

def mean(np_array):
    '''Your code here'''
    m = 0
    for i in np_array:
        m += i
    ans = m/len(np_array)
    '''Stop coding here'''    
    return ans


def stdev(np_array, mu='none'):
    '''Your code here'''
    sd = 0
    for i in np_array:
        sd += (i-mu)**2
    ans = (sd/len(np_array))**0.5
    '''Stop coding here'''    
    return ans

def sampleMean(np_array):
    ''' Each column represents a feature'''
    '''Your code here'''
    ans = []
    for i in range(len(np_array[0])):
        sm = 0
        for j in range(len(np_array)):
            sm += (np_array[j][i])
        m = float(sm/len(np_array))
        ans.append(m)
    '''Stop coding here'''    
    return ans


def covariance(np_array):
    ''' Each column represents a feature'''
    '''Your code here'''
    ans = []
    mn = sampleMean(np_array)
    for i in range(len(np_array[0])):
        c = []
        for j in range(len(np_array[0])):
            cv = 0
            for k in range(len(np_array)):
                cv += (np_array[k][i]-mn[i])*(np_array[k][j]-mn[j])
            c.append(float(cv/len(np_array)))
        ans.append(c)
    '''Stop coding here'''    
    return ans
