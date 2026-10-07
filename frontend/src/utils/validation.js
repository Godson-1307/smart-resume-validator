export const ALLOWED_EXTENSIONS = ['.pdf', '.doc', '.docx', '.txt'];
export const MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024; // 10MB

export function validateSelectedFile(file) {
  if (!file) {
    return { isValid: false, error: 'Please select a file to upload.' };
  }

  const fileName = file.name.toLowerCase();
  const hasValidExt = ALLOWED_EXTENSIONS.some(ext => fileName.endsWith(ext));

  if (!hasValidExt) {
    return {
      isValid: false,
      error: `Unsupported file format. Please upload a PDF, DOCX, or DOC file.`,
    };
  }

  if (file.size > MAX_FILE_SIZE_BYTES) {
    const sizeInMB = (file.size / (1024 * 1024)).toFixed(1);
    return {
      isValid: false,
      error: `File size exceeds 10 MB (current size: ${sizeInMB} MB). Please choose a smaller file.`,
    };
  }

  return { isValid: true, error: null };
}

export function formatFileSize(bytes) {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
}
