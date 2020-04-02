import cv2
from skimage import io


def read_image_opencv():
    # opencv
    # Abrir
    image = cv2.imread("../imagens/frutas.png")
    # Mostrar
    cv2.imshow("Nome Tela", image)
    # Fechar
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# read_image_opencv()
#-----------------

def read_image_skimage():
    # Skimage
    # Abrir
    image_skimage = io.imread("../imagens/frutas.png")
    # Mostrar
    io.imshow(image_skimage)
    io.show()
# read_image_skimage()
#-------------------

# Open-cv abrir video
def read_video_opencv():
    video = cv2.VideoCapture("../videos/formas-geometricas-480.mov")
    fps = video.get(cv2.CAP_PROP_FPS)

    while True:
        ret, frame = video.read()
        #ret retorna se tem frame waitKey controlada o fps e a entrada que para
        if not ret or cv2.waitKey(int(fps)) & 0xFF == ord('q'):
            break
        cv2.imshow("Video", frame)  # lê a imagem atual

    video.release()  # fecha o arquivo
    cv2.destroyAllWindows()


read_video_opencv()


def read_webcam_opencv():
    video = cv2.VideoCapture(0) #0 se tiver uma webcam/ 1 para a segunda webcam...

    while True:
        ret, frame = video.read()
        cv2.imshow("Video", frame)  # lê a imagem atual
        if cv2.waitKey(1) & 0xFF == ord("q"): #controlada o fps da aplicação
            break

    video.release()  # fecha o arquivo
    cv2.destroyAllWindows()
