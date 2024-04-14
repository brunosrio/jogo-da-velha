(def ini-tabuleiro (vec (repeat 3 (vec (repeat 3 "*")))))

(def ini-estado
  {
    :tab ini-tabuleiro
    :vitX 0
    :vitO 0
    :empt 0
    :x-ou-o "X"
 })

(defn alterar-placar [estado vitX? vitO?]
  (cond
    vitX? (update-in estado [:vitX] inc)
    vitO? (update-in estado [:vitO] inc)
    :else (update-in estado [:empt] inc)))

(defn alterar-tabuleiro [estado posicao]
  (let [linha (Integer/parseInt (nth posicao 0)) coluna (Integer/parseInt (nth posicao 1))]
    (assoc-in estado [:tab linha coluna] (get estado :x-ou-o))))

(defn get-tabuleiro [tabuleiro]
  (let [linhas (for [i (range 3)]
                 (str (get-in tabuleiro [i 0]) " | "
                      (get-in tabuleiro [i 1]) " | "
                      (get-in tabuleiro [i 2])
                      "\n" (apply str (repeat 11 "-")) "\n"))]
    (apply str linhas)))

(defn get-placar [estado]
    (str "vitorias de X: " (get estado :vitX) " | "
         "vitorias de O: " (get estado :vitO) " | "
         "empates: " (get estado :empt)))

(defn get-empate-msg [estado]
  (str (apply str (repeat 10 "=")) "\nEMPATE\n" (apply str (repeat 10 "="))
       "\n" (get-tabuleiro (get estado :tab))))

(defn get-vitoria-msg [estado]
  (str (apply str (repeat 15 "=")) "\nVitoria de " (get estado :x-ou-o) "\n" (apply str (repeat 15 "=")) "\n"
       (get-tabuleiro (get estado :tab)) "\n"))

(defn msg-inicial [estado]
  (str (get-placar estado) "\n"
        "\n"(get-tabuleiro (get estado :tab)) "\n"
       "Jogador da vez: " (get estado :x-ou-o) "\n"
        "Insira a linha(0 a 2) e coluna(0 a 2) ex: 1 2 \n(q para sair)"))

(defn fila-igual? [fila]
  (if (not= (nth fila 0) "*")
    (apply = fila)
    false))

(defn tem-linha-igual? [tabuleiro]
  (loop [linha 0] (if (< linha 3)
                  (let [fila (nth tabuleiro linha)]
                    (if (fila-igual? fila) true (recur (inc linha)))) false)))

(defn tem-coluna-igual? [tabuleiro]
  (loop [col 0] (if (< col 3)
    (let [fila [(get-in tabuleiro [0 col]) (get-in tabuleiro [1 col]) (get-in tabuleiro [2 col])]]
      (if (fila-igual? fila) true (recur (inc col)))) false)))

(defn tem-diagonal-igual? [tabuleiro]
  (let [principal [(get-in tabuleiro [0 0]) (get-in tabuleiro [1 1]) (get-in tabuleiro [2 2])]
        secundaria [(get-in tabuleiro [0 2]) (get-in tabuleiro [1 1]) (get-in tabuleiro [2 0])]]
    (cond
      (fila-igual? principal) true
      (fila-igual? secundaria) true
      :else false)))

(defn vitoria? [tabuleiro]
  (cond
    (tem-linha-igual? tabuleiro) true
    (tem-coluna-igual? tabuleiro) true
    (tem-diagonal-igual? tabuleiro) true
    :else false))

(defn empate? [tabuleiro]
  (loop [i 0]
    (if (< i 3)
      (let [fila (nth tabuleiro i)]
        (if (some #(= % "*") fila)
          false
          (recur (inc i))))
      true)))

(defn define-ganhador [estado]
  (cond
    (= (get estado :x-ou-o) "X") (update-in estado [:vitX] inc)
    :else (update-in estado [:vitO] inc)))

(defn main
  ([] (main ini-estado))
  ([estado]
  ((println (msg-inicial estado))
   (let [entrada (read-line)]
     (if (= entrada "q")
       (do
         (println (get-placar estado))
         (System/exit 0))
       (do
         (let [posicao (clojure.string/split entrada #" ") novo-estado (alterar-tabuleiro estado posicao)]
           (if (vitoria? (get novo-estado :tab))
             (let [estado-vitoria (define-ganhador novo-estado)]
               (println (get-vitoria-msg estado-vitoria))
               (main (assoc-in estado-vitoria [:tab] ini-tabuleiro)))
             (if (empate? (get novo-estado :tab))
               (let [estado-empate (alterar-placar novo-estado false false)]
                 (println (get-empate-msg estado-empate))
                 (main (assoc-in estado-empate [:tab] ini-tabuleiro)))
               (main (assoc-in novo-estado [:x-ou-o] (if (= (get novo-estado :x-ou-o) "X") "O" "X"))))))))))))

(main)





















