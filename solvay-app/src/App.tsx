import React, { useRef, useState } from "react";
import { css } from "@emotion/react";
import styled from "@emotion/styled";

const StyledApp = styled.div(
  () => css`
    width: 100vw;
    height: 600px;

    svg {
      background: #eee;

      @keyframes draw {
        from {
          stroke-dashoffset: 1;
        }
        to {
          stroke-dashoffset: 0;
        }
      }

      .heart {
        stroke-dasharray: 1;
        stroke-dashoffset: 1;
        stroke: red;
        stroke-width: 5;
        fill: none;
        animation: draw 5s linear alternate infinite;
      }
    }
  `
);

interface MediaItem {
  type: "image" | "video";
  src: string;
  alt: string;
  marginTop?: string;
  marginLeft?: string;
  marginRight?: string;
}

export function App() {
  const ref = useRef<HTMLVideoElement>(null);
  const [playing, setPlaying] = useState(false);
  const [mediaIndex, setMediaIndex] = useState(0);
  const medias: MediaItem[] = [
    {
      type: "image",
      src: "./images/solvay-color.png",
      alt: "Solvay Color",
      marginTop: "4.6vw",
      marginLeft: "0vw",
      marginRight: "0vw",
    },
    {
      type: "image",
      src: "./images/solvay-bw.jpg",
      alt: "Solvay BW",
      marginTop: "0vw",
      marginLeft: "0vw",
      marginRight: "0vw",
    },
    {
      type: "video",
      src: "./images/solvay-ai.mp4",
      alt: "Solvay AI",
      marginTop: "4.6vw",
      marginLeft: "1.25vw",
      marginRight: "3.25vw",
    },
  ];

  const handlePlay = () => {
    if (ref.current) {
      (ref.current as HTMLVideoElement).play();
      setPlaying(true);
    }
  };

  const handlePause = () => {
    setPlaying(false);
  };

  const handleKeyDown = (e: KeyboardEvent) => {
    if (e.key === "ArrowRight") {
      setMediaIndex((prev) => (prev + 1) % medias.length);
      setPlaying(false);
    } else if (e.key === "ArrowLeft") {
      setMediaIndex((prev) => (prev - 1 + medias.length) % medias.length);
      setPlaying(false);
    }
  };

  React.useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    return () => {
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, []);

  const currentMedia = medias[mediaIndex];
  const computedWidth = `calc(100vw - ${currentMedia.marginLeft} - ${currentMedia.marginRight})`;
  console.log("Rendering media index:", mediaIndex, currentMedia, computedWidth);

  return (
    <StyledApp>
      {currentMedia.type === "image" ? (
        <img
          src={currentMedia.src}
          alt={currentMedia.alt}
          style={{
            width: computedWidth,
            display: "block",
            marginTop: currentMedia.marginTop,
            marginLeft: currentMedia.marginLeft,
            marginRight: currentMedia.marginRight,
          }}
        />
      ) : (
        <div
          style={{
            position: "relative",
            width: computedWidth,
            maxWidth: "100%",
            marginTop: currentMedia.marginTop,
            marginLeft: currentMedia.marginLeft,
            marginRight: currentMedia.marginRight,
          }}
        >
          <video
            ref={ref}
            src={currentMedia.src}
            width="100%"
            style={{ display: "block" }}
            onPlay={() => setPlaying(true)}
            onPause={handlePause}
            controls={false}
          />
          {!playing && (
            <button
              onClick={handlePlay}
              style={{
                position: "absolute",
                top: "50%",
                left: "50%",
                transform: "translate(-50%, -50%)",
                fontSize: "2rem",
                background: "rgba(0,0,0,0.6)",
                color: "white",
                border: "none",
                borderRadius: "50%",
                width: "64px",
                height: "64px",
                cursor: "pointer",
              }}
              aria-label="Play video"
            >
              ▶
            </button>
          )}
        </div>
      )}
    </StyledApp>
  );
}
