import axios from "axios";
import {
  GoogleWebSearchRequest,
  GoogleWebSearchResponse,
  GoogleImageSearchRequest,
  GoogleImageSearchResponse,
} from "../types/search";

const apiKey = process.env.GOOGLE_API_KEY || "";
const cx = process.env.GOOGLE_CX_KEY || "";

/**
 * Calls Google Custom Search API with the given query for web results.
 * @param params GoogleWebSearchRequest
 * @returns GoogleWebSearchResponse
 */
export async function googleWebSearch(
  params: GoogleWebSearchRequest,
): Promise<GoogleWebSearchResponse> {
  if (!apiKey || !cx) {
    throw new Error("Google API credentials not configured. Please set GOOGLE_API_KEY and GOOGLE_CX_KEY environment variables.");
  }

  const {
    query,
    num = 10,
    cr,
    gl,
    siteSearch,
    exactTerms,
    dateRestrict,
  } = params;

  const url = "https://www.googleapis.com/customsearch/v1";
  const response = await axios.get<GoogleWebSearchResponse>(url, {
    params: {
      key: apiKey,
      cx,
      q: query,
      num,
      cr,
      gl,
      siteSearch,
      exactTerms,
      dateRestrict,
    },
  });
  return response.data;
}

/**
 * Calls Google Custom Search API for image search with the given query.
 * @param params GoogleImageSearchRequest
 * @returns GoogleImageSearchResponse
 */
export async function googleImageSearch(
  params: GoogleImageSearchRequest,
): Promise<GoogleImageSearchResponse> {
  if (!apiKey || !cx) {
    throw new Error("Google API credentials not configured. Please set GOOGLE_API_KEY and GOOGLE_CX_KEY environment variables.");
  }

  const {
    query,
    num = 10,
    start = 1,
    safe = "active",
    imgSize,
    imgType,
    imgColorType,
    imgDominantColor,
  } = params;

  const axiosInstance = axios.create({
    baseURL: "https://www.googleapis.com/customsearch/v1",
  });

  const response = await axiosInstance.get<GoogleImageSearchResponse>("", {
    params: {
      q: query,
      searchType: "image",
      key: apiKey,
      cx: cx,
      num: num,
      start: start,
      safe: safe,
      imgSize,
      imgType,
      imgColorType,
      imgDominantColor,
    },
  });

  return response.data;
}
