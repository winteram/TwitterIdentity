j=3
    
    for word in sorted_G1:
        count=0
        if len(K_final1)==200:
            break
        for users in WordsByUser[0]:
            if word[0] in users:
                count=count+1
                if count == j:
                    K_final1.append(word)
                    break
    
    for word in sorted_G2:
        count=0
        if len(K_final2)==200:
            break
        for users in WordsByUser[1]:
            if word[0] in users:
                count=count+1
                if count == j:
                    K_final2.append(word)
                    break
    
    
    K_final=[K_final1,K_final2]