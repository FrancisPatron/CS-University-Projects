(define (sumlist x)
  (cond
    ((null? x) 0)
    (else (+ (car x) (sumlist (cdr x))))
  )
)