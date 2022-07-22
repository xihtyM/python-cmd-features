/* C Bool Library */

/* True/False/Bool */

#if !defined(__cplusplus) && !defined(__STDBOOL_H) && !defined(__BOOL_H)
    #define __BOOL_H

    #ifdef bool
        #undef bool
    #endif

    #ifdef true
        #undef true
    #endif

    #ifdef false
        #undef false
    #endif

    #define bool _Bool
    #define true 1
    #define false 0

    #define true_false_defined true
#endif
