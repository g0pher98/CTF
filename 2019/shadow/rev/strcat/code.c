int sub_401040()
{
  int v0; // ecx
  int v1; // edx
  int v2; // ecx
  char v3; // al
  char v4; // al
  int i; // ecx
  int v6; // edx
  int v7; // ecx
  int v8; // edx
  char v9; // cl
  int v10; // eax
  int v11; // ecx
  char v12; // al
  bool v13; // zf
  char v14; // cl
  int v15; // eax
  __int128 v17; // [esp+0h] [ebp-1A4h]
  char Dst[100]; // [esp+10h] [ebp-194h]
  char v19[100]; // [esp+74h] [ebp-130h]
  char Buffer[99]; // [esp+D8h] [ebp-CCh]
  char v21; // [esp+13Bh] [ebp-69h]
  char v22[100]; // [esp+13Ch] [ebp-68h]

  memset(Dst, 0, 0x64u);
  sub_401010("Input String: ");
  gets(Buffer);
  sub_401010("A: %s\n", Buffer);
	
	
	
  v0 = 0;
  v1 = 0;
  if ( Buffer[0] )
  {
    do
      ++v0;
    while ( Buffer[v0] );
  }
  v2 = v0 - 1;
  do
  {
    v3 = Buffer[v2];
    ++v1;
    --v2;
    *(&v21 + v1) = v3;
  }
  while ( v2 != -1 );
  v22[v1] = 0;
  sub_401010("B: %s\n", v22);
	
	
  v4 = Buffer[0];
  for ( i = 0; v4; v4 = Buffer[i] )
    v19[i++] = v4;
  v19[i] = 58;
  v6 = 0;
  v7 = i + 1;
  if ( v22[0] )
  {
    do
    {
      v19[v7 + v6] = v22[v6];
      ++v6;
    }
    while ( v22[v6] );
  }
  v19[v6 + v7] = 0;
  sub_401010("C: %s\n", v19);
	

	
	
  v17 = xmmword_402130;
  v8 = strcmp(Buffer, v22);
  if ( v8 )
    v8 = -(v8 < 0) | 1;
  if ( !v8 )
  {
    v9 = 21;
    v10 = 0;
    do
    {
      Dst[v10++] = v9;
      v9 = *((_BYTE *)&v17 + v10);
    }
    while ( v9 );
  }
  if ( v8 == 1 && v22[0] )
  {
    v11 = 0;
    do
    {
      v12 = v22[v11++];
      v13 = v22[v11] == 0;
      *((_BYTE *)&v17 + v11 + 15) = v12;
    }
    while ( !v13 );
  }
  if ( v8 == -1 )
  {
    v14 = Buffer[0];
    if ( Buffer[0] )
    {
      v15 = 0;
      do
      {
        Dst[v15++] = v14;
        v14 = Buffer[v15];
      }
      while ( v14 );
    }
  }
  sub_401010("D: %s\n", Dst);
  return 0;
}