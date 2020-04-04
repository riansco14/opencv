import cv2

# Abrindo imagem RGB
image = cv2.imread("../imagens/frutas.png")

# Valores de resolução e quantidade de canais da imagem
imageInformatio = image.shape
print(image.shape)
# Vai retornar  (linhas/altura/height, colunas/largura/width, canais), caso n seja regular ficará sem valor no campo


# Acessando pixels
print("O valor dos pixels é: ", image[150, 150])
# Retorna 3 valores pro ser RGB: [120,170,12] -> [B,G,R]

# Alterando valores das cores [y, x, channel] -> [linha/altura, coluna/largura, channel]
image[150, 150] = [255, 255, 255]  # mandando o vetor com as cores rgb
image[150, 150, 2] = 100  # modificando apenas um canal
image[200:300, 100:150] = [0, 255, 0]  # modificando as cores em um retangulo

cv2.imshow("Imagem", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
