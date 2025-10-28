"use client";

import { C1Chat, ThemeProvider } from "@thesysai/genui-sdk";
import "@crayonai/react-ui/styles/index.css";
import { Theme, themePresets } from "@crayonai/react-ui";

export type ThemeFont =
  | "Inter"
  | "Roboto"
  | "Plus Jakarta Sans"
  | "Open Sans"
  | "Bitter"
  | "Merriweather"
  | "Playfair Display"
  | "Crimson Text"
  | "Geist"
  | "Figtree"
  | "Manrope"
  | "Work Sans"
  | "DM Sans"
  | "IBM Plex Serif"
  | "Space Mono"
  | "Geist Mono"
  | "Host Grotesk";

const generateTypography = () => ({
  fontPrimary: `400 16px/20px Open Sans`,
  fontHeadingLarge: `600 28px/32.2px Open Sans`,
  fontHeadingMedium: `600 24px/27.6px Open Sans`,
  fontHeadingSmall: `500 18px/22.5px Open Sans`,
  fontTitle: `500 16px/20px Open Sans`,
  fontTitleMedium: `500 16px/20px Open Sans`,
  fontTitleSmall: `500 16px/20px Open Sans`,
  fontBody: `400 16px/24px Open Sans`,
  fontBodyLargeHeavy: `500 18px/27px Open Sans`,
  fontBodyLarge: `400 18px/27px Open Sans`,
  fontBodyMedium: `400 16px/20px Open Sans`,
  fontBodySmall: `400 14px/21px Open Sans`,
  fontBodyHeavy: `500 16px/24px Open Sans`,
  fontBodySmallHeavy: `600 16px/20px Open Sans`,
  fontBodyLink: `500 16px/24px Open Sans`,
  fontLabelLarge: `400 16px/19.2px Open Sans`,
  fontLabelLargeHeavy: `500 16px/19.2px Open Sans`,
  fontLabel: `400 14px/16.8px Open Sans`,
  fontLabelHeavy: `500 14px/16.8px Open Sans`,
  fontLabelMedium: `400 16px/20px Open Sans`,
  fontLabelMediumHeavy: `600 16px/20px Open Sans`,
  fontLabelSmall: `400 12px/14.4px Open Sans`,
  fontLabelSmallHeavy: `500 12px/14.4px Open Sans`,
  fontLabelExtraSmall: `400 10px/12px Open Sans`,
  fontLabelExtraSmallHeavy: `500 10px/12px Open Sans`,
  shadowS: "0px 1px 2px rgba(0, 0, 0, 0.04)",
  shadowM: "0px 4px 6px rgba(0, 0, 0, 0.04)",
  shadowL: "0px 1px 8px rgba(0, 0, 0, 0.08)",
  shadowXl: "0px 10px 15px rgba(0, 0, 0, 0.1)",
});

const theme = {
  ...themePresets.classic.darkTheme,
  ...generateTypography(),
} as Theme;

export default function Home() {
  return (
    <ThemeProvider theme={theme}>
      <C1Chat apiUrl="/api/chat" />
    </ThemeProvider>
  );
}
