Claro. Aqui está um **resumo prático das principais sintaxes do Markdown**, organizado como uma pequena folha de consulta.

# Markdown — Resumo

## 1. Títulos

Use `#` no início da linha:

```markdown
# Título 1
## Título 2
### Título 3
#### Título 4
##### Título 5
###### Título 6
```

Resultado:

# Título 1

## Título 2

### Título 3

---

## 2. Negrito e itálico

```markdown
**negrito**
__negrito__

*itálico*
_itálico_

***negrito e itálico***
```

Resultado:

**negrito**

*itálico*

***negrito e itálico***

---

## 3. Tachado

```markdown
~~texto riscado~~
```

Resultado:

~~texto riscado~~

---

## 4. Parágrafos e quebra de linha

Parágrafos são separados por uma linha vazia:

```markdown
Primeiro parágrafo.

Segundo parágrafo.
```

Para forçar uma quebra de linha, normalmente use dois espaços no final:

```markdown
Primeira linha.  
Segunda linha.
```

---

## 5. Listas

### Lista não ordenada

```markdown
- Item
- Item
- Item
```

ou:

```markdown
* Item
* Item
* Item
```

Resultado:

* Item
* Item
* Item

### Lista ordenada

```markdown
1. Primeiro
2. Segundo
3. Terceiro
```

Resultado:

1. Primeiro
2. Segundo
3. Terceiro

### Lista aninhada

```markdown
- Java
  - Spring
  - JPA
- PHP
  - Laravel
```

---

## 6. Links

```markdown
[Google](https://www.google.com)
```

Resultado:

[Google](https://www.google.com)

Também é possível usar o link diretamente:

```markdown
https://www.google.com
```

---

## 7. Imagens

```markdown
![Descrição da imagem](https://exemplo.com/imagem.png)
```

A estrutura é:

```text
![texto alternativo](URL)
```

---

## 8. Código

### Código inline

Use uma crase:

```markdown
Use `System.out.println()` para imprimir.
```

Resultado:

Use `System.out.println()` para imprimir.

### Bloco de código

Use três crases:

````markdown
```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Olá");
    }
}
```
````

O nome depois das três crases especifica a linguagem:

```text
java
javascript
typescript
python
php
c
cpp
sql
bash
json
html
css
```

---

## 9. Citações

Use `>`:

```markdown
> Esta é uma citação.
```

Resultado:

> Esta é uma citação.

Pode aninhar:

```markdown
> Citação principal
>> Citação dentro da citação
```

---

## 10. Linha horizontal

```markdown
---
```

ou:

```markdown
***
```

Resultado:

---

## 11. Tabelas

```markdown
| Nome | Idade | Linguagem |
|------|------:|-----------|
| João | 25 | Java |
| Maria | 30 | PHP |
```

Resultado:

| Nome  | Idade | Linguagem |
| ----- | ----: | --------- |
| João  |    25 | Java      |
| Maria |    30 | PHP       |

### Alinhamento

```markdown
| Esquerda | Centro | Direita |
|:---------|:------:|--------:|
| A | B | C |
```

* `:---` → esquerda
* `:---:` → centro
* `---:` → direita

---

## 12. Checkbox / tarefas

```markdown
- [ ] Fazer exercício
- [x] Estudar Java
- [ ] Estudar Spring
```

Resultado:

* [ ] Fazer exercício
* [x] Estudar Java
* [ ] Estudar Spring

Muito usado em README e listas de estudo.

---

## 13. Escapar caracteres

Se você quiser mostrar um caractere que normalmente possui significado no Markdown, use `\`:

```markdown
\*texto\*
```

Resultado:

*texto*

Caracteres comuns que podem ser escapados:

```text
\* \_ \# \- \+ \. \! \[ \] \( \) \> \`
```

---

## 14. HTML dentro do Markdown

A maioria dos interpretadores permite HTML:

```markdown
<strong>Negrito</strong>

<br>

<details>
<summary>Clique para expandir</summary>

Conteúdo escondido.

</details>
```

Isso é particularmente útil em **README do GitHub**, embora a disponibilidade de HTML dependa do interpretador Markdown.

---

## 15. Comentários HTML

Para colocar uma anotação que não aparece no resultado:

```markdown
<!-- Este texto não será exibido -->
```

---

## 16. Código pré-formatado

Você pode usar quatro espaços para criar um bloco de código:

```markdown
    public static void main(String[] args) {
        System.out.println("Olá");
    }
```

Atualmente, porém, **três crases** são geralmente preferíveis porque permitem especificar a linguagem.

---

# Cheat Sheet

| Objetivo          | Markdown              |
| ----------------- | --------------------- |
| Título            | `# Título`            |
| Subtítulo         | `## Título`           |
| Negrito           | `**texto**`           |
| Itálico           | `*texto*`             |
| Negrito + itálico | `***texto***`         |
| Tachado           | `~~texto~~`           |
| Link              | `[texto](URL)`        |
| Imagem            | `![alt](URL)`         |
| Código inline     | `` `código` ``        |
| Bloco de código   | ` ``` `               |
| Citação           | `> texto`             |
| Lista             | `- item`              |
| Lista numerada    | `1. item`             |
| Checkbox          | `- [ ] tarefa`        |
| Checkbox marcado  | `- [x] tarefa`        |
| Linha horizontal  | `---`                 |
| Tabela            | `\| A \| B \|`        |
| Comentário        | `<!-- comentário -->` |
| Escape            | `\*`                  |

### Uma observação importante

Markdown **não possui exatamente "tags"**, como HTML. Ele é uma **linguagem de marcação baseada em sintaxe**. Por exemplo:

```html
<strong>Java</strong>
```

é HTML com uma *tag* `strong`, enquanto:

```markdown
**Java**
```

é Markdown usando uma **sintaxe de ênfase**.

E existem diferentes "dialetos" de Markdown — CommonMark, GitHub Flavored Markdown (GFM), etc. Por isso, recursos como tabelas, checkboxes e HTML podem variar conforme onde o Markdown é renderizado.
