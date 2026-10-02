import Image from "next/image";

export default function Topo({ titulo, subtitulo, children }: { titulo: string; subtitulo?: string; children?: React.ReactNode }) {
  return (
    <header className="bg-azul text-white">
      <div className="mx-auto flex max-w-6xl items-center gap-3 px-4 py-3 sm:px-8">
        <Image src="/selo.jpg" alt="" width={36} height={36} className="rounded-full" />
        <div className="min-w-0 flex-1">
          <p className="truncate font-display text-lg leading-tight font-bold sm:text-xl">{titulo}</p>
          {subtitulo && <p className="truncate text-sm text-[#d7def2]">{subtitulo}</p>}
        </div>
        {children}
      </div>
    </header>
  );
}
