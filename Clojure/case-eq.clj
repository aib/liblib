(defmacro case=-impl [value & clauses]
  (when clauses
    (if (next clauses)
        `(if (= ~value ~(first clauses))
             ~(second clauses)
             (case=-impl ~value ~@(next (next clauses))))
        (first clauses))))

(defmacro case= [value & clauses]
  `(let [v# ~value] (case=-impl v# ~@clauses)))
